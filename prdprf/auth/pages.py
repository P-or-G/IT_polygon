import reflex as rx

from reflex_local_auth.pages.registration import RegistrationState, register_form

from prdprf import navigation
from prdprf.ui.base import base_page

from prdprf.auth.forms import my_register_form, my_login_form
from prdprf.auth.state import SessionState, MyLoginState


def my_login_page():
    return rx.center(
            rx.cond(
                MyLoginState.is_hydrated,
                rx.card(my_login_form()),
            ),
            min_height="85vh",
        ),


def my_register_page() -> rx.Component:
    return rx.center(
            rx.cond(
                RegistrationState.success,
                rx.vstack(
                    rx.text("Регистрация прошла успешно!"),
                ),
                rx.card(my_register_form()),

            ),
            min_height="85vh",
        )


def my_logout_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Вы уверены, что хотите выйти", size="7"),
        rx.link(
            rx.button("Не-а", color_scheme="gray"),
            href=navigation.routes.HOME_ROUTE
        ),
        rx.button("Да, я хочу выйти", on_click=SessionState.perform_logout),
        spacing="5",
        justify="center",
        align="center",
        # text_align="center",
        min_height="85vh",
        id='my-child'
    )
    return base_page(my_child)
