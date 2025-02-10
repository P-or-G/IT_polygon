import reflex as rx
from typing import List

from sqlmodel import select

from prdprf.auth.state import SessionState
from prdprf.models import Question


class VariantState(rx.State):
    tasks_number: int = 10
    tasks: list

    def load_tasks(self):
        with rx.session() as session:
            result = session.exec(
                select(Question).limit(5)
            ).all()
            self.tasks = result

    @rx.event
    def on_submit(self, form):
        print(form)


def variant_form(question: Question):
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.text(f'Вес: {question.score}'),
                rx.text(question.subject)),
            rx.text(question.question),
            rx.input("Ответ", placeholder="Ответ"),
            rx.button("Ответить"),
            padding='1em',
            width="1000px",
        ),
        on_submit=VariantState.on_submit
    )
