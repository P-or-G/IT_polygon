import reflex as rx
import reflex_local_auth

from prdprf import navigation


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )



def navbar() -> rx.Component:
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
                    navbar_link("Главная страница", navigation.routes.HOME_ROUTE),
                    navbar_link("О нас", navigation.routes.ABOUT_US_ROUTE),
                    navbar_link("Уроки", navigation.routes.ARTICLE_LIST_ROUTE),
                    navbar_link("Контакты", navigation.routes.CONTACT_US_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Регистрация",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE
                    ),
                    rx.link(
                        rx.button(
                            "Вход",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id='my-navbar-hstack-desktop',
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "It-полигон", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Главная страница",
                                     on_click=navigation.NavState.to_home),
                        rx.menu.item("О нас",
                                     on_click=navigation.NavState.to_about_us),
                        rx.menu.item("Уроки",
                                     on_click=navigation.NavState.to_articles),
                        rx.menu.item("Contact",
                                     on_click=navigation.NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Вход",
                                     on_click=navigation.NavState.to_login),
                        rx.menu.item("Регистрация",
                                     on_click=navigation.NavState.to_register),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id='my-main-nav',
    )
