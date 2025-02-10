import reflex as rx
import reflex_local_auth

from prdprf import navigation
from prdprf.auth.state import SessionState, MyLocalAuthState
from prdprf.ui.base import base_page


def logout_item() -> rx.Component:

    return rx.box(
        rx.hstack(
            rx.icon("log-out"),
            rx.text("Выйти", size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "cursor": "pointer", # css
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "color": rx.color("accent", 11),
                "border-radius": "0.5em",
            },
        ),
        on_click=navigation.NavState.to_logout,
        as_='button',
        underline="none",
        weight="medium",
        width="100%",
    )


def profile_card() -> rx.Component:
    user_info_obj = SessionState.authenticated_user_info
    username_via_user_obj = rx.cond(SessionState.authenticated_username, SessionState.authenticated_username, "Имя")
    surname_via_user_obj = rx.cond(SessionState.authenticated_surname, SessionState.authenticated_surname, "Фамилия")
    grade_via_user_obj = rx.cond(SessionState.authenticated_grade, SessionState.authenticated_grade, "Класс")
    litera_via_user_obj = rx.cond(SessionState.authenticated_litera, SessionState.authenticated_litera, "Литера")
    points_via_user_obj = rx.cond(SessionState.authenticated_points, SessionState.authenticated_points, "0")
    return rx.center(
        rx.vstack(
            rx.heading(f"{username_via_user_obj} {surname_via_user_obj}", size="9"),
            rx.spacer(),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text(f"Ваш класс: {grade_via_user_obj} {litera_via_user_obj}", align="left", weight="medium"),
                        rx.text(f"Ваш счёт: {points_via_user_obj}", align="right", weight="medium")
                    ),
                    rx.button(
                        rx.text(f"Ваш статус: {rx.cond(MyLocalAuthState.status, 'Учитель', 'Ученик')}"),
                        on_double_click=SessionState.status_change
                    ),
                ),
            ),
            spacing="8",
            border=f"1.5px solid {rx.color('gray', 5)}",
            background=rx.color("gray", 1),
            padding="28px",
            width="100%",
            max_width="400px",
            min_height="475px",
            border_radius="0.5rem",
            align='center'
        ),
    )


@reflex_local_auth.require_login
def profile_page() -> rx.Component:
    my_child = rx.vstack(profile_card(),
                         spacing="5",
                         justify="center",
                         align="center",
                         min_height="85vh",
                         id='my-child'
                         )
    return base_page(my_child)
