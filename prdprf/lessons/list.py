import reflex as rx 
import reflex_local_auth
from prdprf import navigation
from prdprf.ui.base import base_page
from prdprf.models import BlogPostModel
from prdprf.lessons import state
from prdprf.lessons.quill import QuillDeps


def blog_post_detail_link(child: rx.Component, post: BlogPostModel):
    if post is None:
        return rx.fragment(child)
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.YOUR_LESSONS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    return rx.link(
        child,
        rx.heading("Создано ", post.userinfo.email),
        href=post_detail_url
    )


def blog_post_list_item(post: BlogPostModel):
    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            
            post
        ),
        padding='1em'
    )


@reflex_local_auth.require_login
def blog_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            *QuillDeps,
            rx.heading("Уроки",  size="5"),
            rx.link(
                rx.button("Создать урок"),
                href=navigation.routes.LESSON_ADD_ROUTE
            ),
            rx.foreach(state.BlogPostState.posts, blog_post_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    ) 
