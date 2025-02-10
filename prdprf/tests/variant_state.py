import reflex as rx
from typing import List

from sqlmodel import select

from prdprf.auth.state import SessionState
from prdprf.models import Question


class VariantState(rx.State):
    tasks_number: int = 10
    tasks: list[Question]

    def load_tasks(self):
        with rx.session() as session:
            result = session.exec(
                select(Question).limit(self.tasks_number)
            ).all()
            self.tasks = result

    def on_submit(self, form):
        print(form)


