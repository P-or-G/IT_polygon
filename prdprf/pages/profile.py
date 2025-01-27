import reflex as rx
import reflex_local_auth

from prdprf.auth.state import SessionState
from prdprf.ui.base import base_page


def profile_card() -> rx.Component:
    user_info_obj = SessionState.authenticated_user_info
    username_via_user_obj = rx.cond(SessionState.authenticated_username, SessionState.authenticated_username, "Имя")
    surname_via_user_obj = rx.cond(SessionState.authenticated_surname, SessionState.authenticated_surname, "Фамилия")
    grade_via_user_obj = rx.cond(SessionState.authenticated_grade, SessionState.authenticated_grade, "Класс")
    litera_via_user_obj = rx.cond(SessionState.authenticated_litera, SessionState.authenticated_litera, "Литера")
    points_via_user_obj = rx.cond(SessionState.authenticated_points, SessionState.authenticated_points, "Счёт")
    return rx.vstack(
        rx.heading(f"{username_via_user_obj} {surname_via_user_obj}", size="9"),
        rx.text(),
        spacing = "5",
        justify = "center",
        align = "center",
        min_height = "85vh",
        id = 'my-child'
    )


@reflex_local_auth.require_login
def profile_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Ваш профиль", size="9"),
            rx.text(
                "Something cool about us.",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)
