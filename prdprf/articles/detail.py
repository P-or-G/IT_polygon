import reflex as rx

from prdprf.lessons.detail import html_style_base
from prdprf.lessons.quill import QuillDeps
from prdprf.comments.form import index
from prdprf.ui.base import base_page

from prdprf.articles import state

from prdprf.lessons.notfound import blog_post_not_found


def article_detail_page() -> rx.Component:
    my_child = rx.cond(state.ArticlePublicState.post, rx.vstack(
            rx.hstack(
                rx.heading(state.ArticlePublicState.post.title, size="9"),
                align='end'
            ),
            rx.text("Тема ", state.ArticlePublicState.post.subject),
            rx.text(
                state.ArticlePublicState.post.content,
                white_space='pre-wrap'
            ),
            spacing="5",
            align="center",
            min_height="85vh"
        ), 
        blog_post_not_found()
        )
    my_child = rx.cond(state.ArticlePublicState.post,
                       rx.vstack(
                           *QuillDeps,
                           rx.hstack(
                               rx.heading(state.ArticlePublicState.post.title, size="9"),
                               align='end'
                           ),
                           rx.text("Тема ", state.ArticlePublicState.post.subject),
                           rx.box(
                               rx.html(
                                   html_style_base + state.ArticlePublicState.post.content,
                               ),
                               width="1000px",
                           ),
                           index(),
                           spacing="5",
                           align="center",
                           min_height="85vh",
                       ),
                       blog_post_not_found()
                       )
    return base_page(my_child)
