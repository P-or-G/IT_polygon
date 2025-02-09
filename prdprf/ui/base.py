import reflex as rx

from prdprf.auth.state import SessionState
from prdprf.ui.nav import navbar
from prdprf.ui.dashboard import base_dashboard_page


def base_layout_component(child, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            padding="1em",
            width="100%",
            id="my-content-area-el"
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("Что-то пошло не так")
    return base_dashboard_page(child, *args, **kwargs)
