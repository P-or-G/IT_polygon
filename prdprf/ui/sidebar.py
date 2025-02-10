import reflex as rx
from reflex.style import toggle_color_mode

from prdprf.auth.state import SessionState
from prdprf import navigation


def sidebar_user_item() -> rx.Component:
    user_info_obj = SessionState.authenticated_user_info
    username_via_user_obj = rx.cond(SessionState.authenticated_username, SessionState.authenticated_username, "Имя")
    surname_via_user_obj = rx.cond(SessionState.authenticated_surname, SessionState.authenticated_surname, "Фамилия")
    return rx.cond(
        user_info_obj,
        rx.hstack(
            rx.icon_button(
                rx.icon("user"),
                size="4",
                radius="full",
                on_click=lambda: rx.redirect(navigation.routes.PROFILE_ROUTE),
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        username_via_user_obj + " " + surname_via_user_obj,
                        size="3",
                        weight="bold",
                    ),
                    rx.flex(
                        rx.text(
                            f"{user_info_obj.email}",
                            size="2",
                            weight="medium",
                        ),
                        overflow="hidden",
                    ),
                    width='85%',
                ),
                spacing="0",
                align="start",
                justify="start",
                width="100%",

            ),
            padding_x="0.5rem",
            align="center",
            justify="start",
            width="100%",
        ),
        rx.fragment("")
    )


def sidebar_logout_item(text="Выйти") -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.icon("log-out"),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style=rx.Style(
                {
                    "_hover": {
                        "cursor": "pointer",  # css
                        "bg": rx.color("accent", 4),
                        "color": rx.color("accent", 11),
                    },
                    "color": rx.color("accent", 11),
                    "border-radius": "0.5em",
                },
            )
        ),
        on_click=navigation.NavState.to_logout,
        as_='button',
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_dark_mode_toggle_item() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.color_mode_cond(
                light=rx.icon("moon"),
                dark=rx.icon("sun"),
            ),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style=rx.Style(
                {
                    "_hover": {
                        "cursor": "pointer",  # css
                        "bg": rx.color("accent", 4),
                        "color": rx.color("accent", 11),
                    },
                    "color": rx.color("accent", 11),
                    "border-radius": "0.5em",
                }
            ),
        ),
        on_click=toggle_color_mode,
        as_='button',
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_item(
        text: str, icon: str, href: str,
) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.icon(icon),
            rx.text(text, size="4", align="center", weight='medium'),
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            align_items="center",
            style=rx.Style(
                {
                    "_hover": {
                        "bg": rx.color("accent", 4),
                        "color": rx.color("accent", 11),
                    },
                    "border-radius": "0.5em",
                },
            )
        ),
        href=href,
        underline="none",
        weight="medium",
    )


def mobile_sidebar_item(
        text: str, icon: str, href: str,
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", align="center", weight='medium'),
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            align_items="center",
            style=rx.Style(
                {
                    "_hover": {
                        "bg": rx.color("accent", 4),
                        "color": rx.color("accent", 11),
                    },
                    "border-radius": "0.5em",
                },
            )
        ),
        href=href,
        underline="none",
        weight="medium",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    rx.link(
                        rx.heading(
                            "It-полигон", size="7", weight="bold"
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    sidebar_item("Уроки", "library", navigation.routes.ARTICLE_LIST_ROUTE),
                    rx.cond(SessionState.authenticated_teacher,
                            sidebar_item("Ваши уроки", "book-user", navigation.routes.YOUR_LESSONS_ROUTE), ),
                    rx.cond(SessionState.authenticated_teacher,
                            sidebar_item("Создать задание", "square-plus", navigation.routes.CREATE_TEST_ROUTE), ),
                    sidebar_item("Задания", "book-open-check", navigation.routes.ALL_TESTS_ROUTE),
                    spacing="5"
                ),
                rx.hstack(
                    sidebar_logout_item(text=""),
                    sidebar_dark_mode_toggle_item(),
                    sidebar_user_item(),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            rx.vstack(
                                mobile_sidebar_item("Уроки", "library", navigation.routes.ARTICLE_LIST_ROUTE),
                                mobile_sidebar_item("Тесты", "book-open-check", navigation.routes.ALL_TESTS_ROUTE),
                                rx.cond(SessionState.authenticated_teacher,
                                        mobile_sidebar_item("Ваши уроки", "book-user",
                                                            navigation.routes.YOUR_LESSONS_ROUTE), ),
                                mobile_sidebar_item("Задания", "book-open-check", navigation.routes.ALL_TESTS_ROUTE),
                                spacing="3",
                            ),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_dark_mode_toggle_item(),
                                    sidebar_logout_item(),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                sidebar_user_item(),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
        bg=rx.color("accent"),
        padding="1em",
        width="100%",
    )


def unify_nav_bar() -> rx.Component:
    return rx.box()
