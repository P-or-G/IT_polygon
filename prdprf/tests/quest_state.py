import reflex as rx
import json
from typing import Dict, Any
from prdprf.models import Question


class QuestsState(rx.State):
    selected_quest: Question = None
    new_quest_text: str = ""
    new_quest_answer: str = ""
    new_quest_score: int = 1
    new_quest_subject = "Математика"
    error_message: str = ""

    def select_question(self, question: Question):
        """Выбор теста для просмотра деталей"""
        self.selected_quest = question  # Установка выбранного теста

    def clear_selected_question(self):
        """Сброс выбора теста"""
        self.selected_quest = None

    def handle_text_change(self, text):
        """Обработчик изменения названия нового теста"""
        self.new_quest_text = text

    @rx.event
    def handle_subject_change(self, subject):
        """Обработчик изменения предмета нового теста"""
        self.new_quest_subject = subject

    def handle_answer_change(self, answer):
        """Обработчик изменения предмета нового теста"""
        self.new_quest_answer = answer

    def handle_score_change(self, score):
        """Обработчик изменения предмета нового теста"""
        self.new_quest_score = score

    def add_test(self):
        """Добавление нового теста в базу данных"""
        if self.new_quest_text != "" and self.new_quest_answer != "" and self.new_quest_score != 0:
            with rx.session() as session:  # Создание сессии для работы с базой данных
                new_quest = Question(question=self.new_quest_text,
                                     subject=self.new_quest_subject,
                                     answer=self.new_quest_answer,
                                     score=self.new_quest_score)  # Создание объекта Quest
                session.add(new_quest)  # Добавление теста в базу данных
                session.commit()  # Сохранение изменений

            self.new_quest_text = ""
            self.new_quest_answer = ""
            self.new_quest_score = 1
            self.new_quest_subject = "Математика"
            self.error_message = ""
