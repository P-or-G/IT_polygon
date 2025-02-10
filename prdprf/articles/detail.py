import reflex as rx

from prdprf.lessons.detail import blog_post_detail_page
from prdprf.ui.base import base_page


def article_detail_page() -> rx.Component:
    return blog_post_detail_page()
