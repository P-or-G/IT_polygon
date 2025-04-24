import reflex as rx


class Question(rx.Base):
    question_text: str
    options: list[str]  # Варианты ответов
    correct_answer: str
    subject: str
    difficulty: str

class State(rx.State):
    questions: list[Question] = []
    current_question: Question | None = None
    user_answer: str = ""
    score: int = 0

    def load_questions(self):
        # Загрузка вопросов из БД или JSON
        self.questions = [
            Question(
                question_text="Сколько будет 2+2?",
                options=["3", "4", "5"],
                correct_answer="4",
                subject="Математика",
                difficulty="Лёгкий"
            )
        ]
        self.current_question = self.questions[0]

    def check_answer(self):
        if self.user_answer == self.current_question.correct_answer:
            self.score += 1
        self.next_question()

    def next_question(self):
        # Переход к следующему вопросу (можно рандомизировать)
        index = self.questions.index(self.current_question) + 1
        if index < len(self.questions):
            self.current_question = self.questions[index]
            self.user_answer = ""
