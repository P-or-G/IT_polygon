import reflex as rx

from prdprf.comments.form import index
from prdprf.ui.base import base_page

from prdprf.lessons import state
from prdprf.lessons.quill import QuillDeps
from prdprf.lessons.notfound import blog_post_not_found

html_style_base = '''<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #b9b9b9;
}
</style>'''


def blog_post_detail_page() -> rx.Component:
    can_edit = True
    edit_link = rx.link("Редактировать", href=f"{state.LessonPostState.blog_post_edit_url}")
    edit_link_el = rx.cond(
        can_edit,
        edit_link,
        rx.fragment("")
    )
    my_child = rx.cond(state.LessonPostState.post,
                       rx.vstack(
                           *QuillDeps,
                           rx.hstack(
                               rx.heading(state.LessonPostState.post.title, size="8"),
                               edit_link_el,
                               align='end'
                           ),
                           rx.box(
                               rx.html(
                                   html_style_base + state.LessonPostState.post.content,
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
