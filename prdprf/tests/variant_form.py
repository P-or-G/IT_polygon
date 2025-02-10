import reflex as rx

import reflex_local_auth

from prdprf.auth.state import SessionState
from prdprf.tests.questions_form import add_question_form
from prdprf.tests.subj_state import SubjectListState, question_list_item
from prdprf.ui.base import base_page


@reflex_local_auth.require_login
def variant_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.select(
                ["Математика", "Информатика", "Физика", "Робототехника", "Программирование"],
                value=SubjectListState.category,
                on_change=SubjectListState.category_change,
                position="popper"
            ),
            rx.foreach(SubjectListState.questions, question_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )


@reflex_local_auth.require_login
def question_add_page() -> rx.Component:
    return base_page(rx.cond(SessionState.authenticated_teacher, add_question_form()))
