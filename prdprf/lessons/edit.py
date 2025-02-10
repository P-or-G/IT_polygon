import reflex as rx
import reflex_local_auth
from prdprf.ui.base import base_page

from prdprf.lessons import forms

from prdprf.lessons.state import LessonEditFormState
from prdprf.lessons.notfound import blog_post_not_found


@reflex_local_auth.require_login
def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = LessonEditFormState.post
    my_child = rx.cond(post,
                       rx.vstack(
                           rx.heading("Редактирование ", post.title, size="9"),
                           rx.desktop_only(
                               rx.box(
                                   my_form,
                                   width='50vw'
                               )
                           ),
                           rx.tablet_only(
                               rx.box(
                                   my_form,
                                   width='75vw'
                               )
                           ),
                           rx.mobile_only(
                               rx.box(
                                   my_form,
                                   width='95vw'
                               )
                           ),
                           spacing="5",
                           align="center",
                           min_height="95vh",
                       ),
                       blog_post_not_found()
                       )
    return base_page(my_child)
