"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from prdprf.ui.base import base_page

from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_page,
    additional_register_page,
)
from .auth.state import SessionState

from .articles.detail import article_detail_page
from .articles.list import article_public_list_page
from .articles.state import ArticlePublicState

from . import lessons, navigation, pages
from .tests.subj_page import question_post_list_page, question_add_page
from .tests.subj_state import SubjectListState


def index() -> rx.Component:
    return rx.cond(SessionState.is_authenticated,
                   base_page(pages.dashboard_component(), ),
                   my_register_page()
                   )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="sky"
    )

)

app.add_page(index,
             on_load=ArticlePublicState.load_posts
             )

app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

app.add_page(
    pages.profile_page,
    route=navigation.routes.PROFILE_ROUTE,
    on_load=SessionState.on_load
)

app.add_page(
    article_public_list_page,
    route=navigation.routes.ARTICLE_LIST_ROUTE,
    on_load=ArticlePublicState.load_posts
)

app.add_page(
    article_detail_page,
    route=f"{navigation.routes.ARTICLE_LIST_ROUTE}/[p_id]",
    on_load=ArticlePublicState.get_post_detail
)

app.add_page(
    lessons.blog_post_list_page,
    route=navigation.routes.YOUR_LESSONS_ROUTE,
    on_load=lessons.BlogPostState.load_posts

)

app.add_page(
    lessons.blog_post_add_page,
    route=navigation.routes.LESSON_ADD_ROUTE
)

app.add_page(
    lessons.blog_post_detail_page,
    route="/lessons/[blog_id]",
    on_load=lessons.BlogPostState.get_post_detail
)

app.add_page(
    lessons.blog_post_edit_page,
    route="/lessons/[blog_id]/edit",
    on_load=lessons.BlogPostState.get_post_detail
)

app.add_page(
    question_post_list_page,
    route=navigation.routes.ALL_TESTS_ROUTE,
    on_load=SubjectListState.load_quests
)

app.add_page(
    question_add_page,
    route=navigation.routes.CREATE_TEST_ROUTE
)

app.add_page(
    additional_register_page,
    route=navigation.routes.REGISTER_OAUTH_ROUTE,
)
