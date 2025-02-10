import reflex as rx

from prdprf.ui.dashboard import base_dashboard_page


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("Что-то пошло не так")
    return base_dashboard_page(child, *args, **kwargs)
