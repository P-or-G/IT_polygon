import reflex as rx

from prdprf.ui.sidebar import sidebar


def base_dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("Что-то пошло не так")
    return rx.fragment( 
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                rx.logo(),
                padding="1em",
                width="100%",
                id="my-content-area-el"
            ),
            
        ),
    )
