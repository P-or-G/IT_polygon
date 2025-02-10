import reflex as rx
from typing import List

from prdprf.auth.state import SessionState
from prdprf.models import Question


class SubjectListState(rx.State):
    questions: List['Question'] = []
    category: str = 'Математика'

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get("blog_id", "")

    def load_quests(self):
        with rx.session() as session:
            print(Question.subject, self.category)
            result = session.exec(
                Question.select().where(Question.subject == self.category)
            ).all()
            self.questions = result

    @rx.event
    def category_change(self, category: str):
        self.category = category
        self.load_quests()


def question_list_item(question: Question):
    return rx.vstack(
        rx.hstack(
            rx.text(f'Вес: {question.score}'),
            rx.text(question.subject)),
        rx.text(question.question),
        rx.cond(
            SessionState.authenticated_teacher,
            rx.tooltip(
                rx.button("Посмотреть ответ"),
                content=question.answer,
            )
        ),
        padding='1em',
        width="1000px",

    )
