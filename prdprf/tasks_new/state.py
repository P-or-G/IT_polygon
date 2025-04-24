from typing import Optional, List
from datetime import datetime, timedelta

import reflex as rx
import sqlalchemy

from prdprf.lessons.state import LessonEditFormState
from prdprf.models import Question, TestQuestionLink, TestModel


class QuestionState(rx.State):
    # Текущий вопрос и ответ пользователя
    current_question: Question = Question()  # Инициализация пустым объектом
    user_answer: str = ""
    score: int = 0
    current_test_id: int = -1  # ID активного теста

    def load_question_from_test(self, test_id: int):
        """Загружает следующий вопрос из конкретного теста."""
        with rx.session() as session:
            # Получаем все вопросы теста с сортировкой по order
            questions = session.exec(
                sqlalchemy.select(Question)
                .join(TestQuestionLink)
                .where(TestQuestionLink.test_id == test_id)
                .order_by(TestQuestionLink.order)
            ).all()

            if questions:
                self.current_question = questions[0]  # Первый вопрос
                self.current_test_id = test_id

    def check_answer(self):
        """Проверяет ответ и переходит к следующему вопросу в тесте."""
        if self.user_answer == self.current_question.answer:
            self.score += self.current_question.score

        # Загружаем следующий вопрос из того же теста
        with rx.session() as session:
            next_question = session.exec(
                sqlalchemy.select(Question)
                .join(TestQuestionLink)
                .where(
                    TestQuestionLink.test_id == self.current_test_id,
                    TestQuestionLink.order > self.current_question.order  # Следующий по порядку
                )
                .order_by(TestQuestionLink.order)
                .limit(1)
            ).first()

            if next_question:
                self.current_question = next_question
            else:
                # Тест завершён
                self.reset_test()

    def reset_test(self):
        """Сброс состояния после завершения теста."""
        self.current_question = Question()
        self.user_answer = ""
        self.current_test_id = -1


class TestState(rx.State):
    current_test: TestModel = TestModel()  # Инициализация пустым объектом
    available_tests: List[TestModel] = []  # Пустой список по умолчанию
    current_questions: List[Question] = []  # Вопросы текущего теста

    # Прогресс
    current_question_index: int = 0  # Начинаем с первого вопроса
    user_answers: List[str] = []  # Пустой список ответов
    start_time: Optional[datetime] = None
    time_left: int = 0  # Таймер по C

    def create_test(
            self,
            title: str,
            subject: str,
            question_ids: List[int],  # ID вопросов для добавления
            time_limit: int = 1800
    ):
        with rx.session() as session:
            # Создаем тест
            test = TestModel(
                title=title,
                subject=subject,
                time_limit=time_limit,
                creator_id=self.user.id
            )
            session.add(test)
            session.commit()

            # Добавляем вопросы в тест
            for order, q_id in enumerate(question_ids):
                session.add(
                    TestQuestionLink(
                        test_id=test.id,
                        question_id=q_id,
                        order=order
                    )
                )
            session.commit()

    # Загрузка вопросов теста
    def load_test_questions(self, test_id: int):
        with rx.session() as session:
            self.current_test = session.exec(
                sqlalchemy.select(TestModel).where(TestModel.id == test_id)
            ).first()

            # Вопросы с сортировкой по order из связующей таблицы
            self.current_questions = session.exec(
                sqlalchemy.select(Question)
                .join(TestQuestionLink)
                .where(TestQuestionLink.test_id == test_id)
                .order_by(TestQuestionLink.order)
            ).all()


class Time(rx.State):
    time_left: int = 15 * 60  # 15 минут

    def tick(self):
        self.time_left -= 1


class QuestionGeneratorState(LessonEditFormState):
    question_text: str = ""
    answers: List[str] = ["", ""]  # Минимум 2 варианта
    correct_answers: List[int] = []  # Выбранные правильные варианты
    difficulty: str = "medium"
    topic: str = ""

    # 1. Метод для обновления конкретного ответа
    def update_answer(self, index: int, value: str):
        self.answers[index] = value
        self.answers = self.answers.copy()  # Принудительное обновление состояния

    # 2. Метод для добавления/удаления ответов
    def add_answer_field(self):
        self.answers.append("")
        self.answers = self.answers.copy()

    def remove_answer_field(self, index: int):
        if len(self.answers) > 2:  # Минимум 2 варианта ответа
            self.answers.pop(index)
            # Обновляем индексы правильных ответов
            self.correct_answers = [
                i if i < index else i - 1
                for i in self.correct_answers
                if i != index
            ]
            self.answers = self.answers.copy()
            self.correct_answers = self.correct_answers.copy()

    # 3. Метод для переключения правильных ответов
    def toggle_correct_answer(self, index: int):
        if index in self.correct_answers:
            self.correct_answers.remove(index)
        else:
            self.correct_answers.append(index)
        self.correct_answers = self.correct_answers.copy()

    def save_question(self):
        with rx.session() as session:
            session.add(
                Question(
                    question_text=self.question_text,
                    answers=self.answers,
                    correct_answers=self.correct_answers,
                    difficulty=self.difficulty,
                    topic=self.topic,
                    creator_id=self.user.id
                )
            )
            session.commit()
        self.reset_question()

    def reset_question(self):
        self.question_text = ""
        self.answers = ["", ""]
        self.correct_answers = []
