import reflex as rx
from typing import Dict, Any

import reflex_local_auth

from prdprf.models import Test, Question
from prdprf.tests.quest_state import QuestsState
from prdprf.tests.questions_form import add_question_form
from prdprf.tests.subj_state import SubjectListState, question_list_item
from prdprf.ui.base import base_page


@reflex_local_auth.require_login
def question_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.foreach(SubjectListState.questions, question_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )


@reflex_local_auth.require_login
def question_add_page() -> rx.Component:
    return base_page(add_question_form())