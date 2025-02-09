import reflex as rx

from prdprf.ui.base import base_page
from prdprf.tests.testsstate import index


def about_page() -> rx.Component:
    return base_page(index())
