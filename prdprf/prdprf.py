import reflex as rx
import reflex_local_auth

from prdprf.ui.base import base_page

from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_page
)
from .auth.protected import profile_page
from .auth.state import SessionState, MyLocalAuthState

from .articles.detail import article_detail_page
from .articles.list import article_public_list_page
from .articles.state import ArticlePublicState

from . import lessons, navigation, dashboard
from .dashboard import page
from .stats.page import loading_data_table_example
from .tasks_new.page import question_generator_form
from .translator.main import translator_page


def index() -> rx.Component:
    return rx.cond(SessionState.is_authenticated,
                   base_page(page.dashboard_component()),
                   my_register_page()
                   )


app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="large",
        accent_color="purple",
        gray_color="gray"
    ),
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
    profile_page,
    route=navigation.routes.PROFILE_ROUTE,
    on_load=MyLocalAuthState.update_value
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
    route=navigation.routes.LESSONS_ROUTE,
    on_load=lessons.LessonPostState.load_posts
)

app.add_page(
    lessons.blog_post_add_page,
    route=navigation.routes.LESSON_ADD_ROUTE
)

app.add_page(
    lessons.blog_post_detail_page,
    route="/lessons/[blog_id]",
    on_load=lessons.LessonPostState.get_post_detail
)

app.add_page(
    lessons.blog_post_edit_page,
    route="/lessons/[blog_id]/edit",
    on_load=lessons.LessonPostState.get_post_detail
)

app.add_page(
    base_page(loading_data_table_example()),
    route=navigation.routes.STATISTICS_ROUTE
)

app.add_page(
    translator_page,
    route=navigation.routes.TRANSLATOR_ROUTE
)

app.add_page(
    question_generator_form,
    route=navigation.routes.TEST_ROUTE,  # /variant
)
