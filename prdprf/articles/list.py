import reflex as rx

from prdprf import navigation
from prdprf.ui import base
from prdprf.models import LessonPostModel
from prdprf.articles import state


def article_card_link(post: LessonPostModel):
    post_id = post.id
    if post_id is None:
        return rx.fragment("Not found")
    root_path = navigation.routes.LESSONS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    return rx.card(
        rx.link(
            rx.flex(
                rx.box(
                    rx.heading(post.title),
                ),
                spacing="2",
            ),
            href=post_detail_url
        ),
        as_child=True,
    )


def article_public_list_component(columns: int = 3, spacing: int = 5, limit: int = 100) -> rx.Component:
    return rx.scroll_area(
        rx.vstack(
            rx.foreach(state.ArticlePublicState.posts, article_card_link),
            columns=f'{columns}',
            spacing=f'{spacing}',
            on_mount=lambda: state.ArticlePublicState.set_limit_and_reload(limit),
            align='center'
        ),
        type="always",
        scrollbars="vertical",
        style=rx.Style({"height": 700}),
    )


def article_public_list_page() -> rx.Component:
    return base.base_page(
        rx.box(
            rx.heading("Уроки",  size="5"),
            article_public_list_component(),
            min_height="85vh",
        )
    ) 
