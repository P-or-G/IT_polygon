import reflex as rx
from typing import Dict, Any, List, Optional

import reflex_local_auth
import sqlalchemy
from reflex import select

from prdprf.models import Test, Question
from prdprf.tests.quest_state import QuestsState
from prdprf.ui.base import base_page


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


def question_list_item(question: Question):
    return rx.vstack(
        rx.hstack(
            rx.text(f'{question.score} баллов'),
            rx.text(question.subject)),
        rx.text(question.question),
        rx.input(
            name='answer',
            type='answer'
        ),
        padding='1em'
    )