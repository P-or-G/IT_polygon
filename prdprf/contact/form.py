import reflex as rx 

from ..auth.state import SessionState
from .state import ContactState


def contact_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.input(
                    name='email',
                    placeholder='Ваша почта',
                    type='email',
                    width='100%',
                ),
                rx.text_area(
                    name='message',
                    placeholder="Ваша проблема",
                    required=True,
                    width='100%',
                ),
                rx.button("Отправить", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )
