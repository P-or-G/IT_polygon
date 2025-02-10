import reflex as rx

import reflex_local_auth

from prdprf.models import Question
from prdprf.tests.variant_state import VariantState
from prdprf.ui.base import base_page


def variant_form(question: Question):
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.text(f'Вес: {question.score}'),
                rx.text(question.subject)),
            rx.text(question.question),
            rx.hstack(
                rx.input(),
                rx.button("Ответить"),
            ),
            padding='1em',
        ),
        align='center',
        on_submit=VariantState.on_submit
    )


@reflex_local_auth.require_login
def variant_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.foreach(VariantState.tasks, variant_form),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )
