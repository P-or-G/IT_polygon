import reflex as rx
from .quill import Quill, ReactQuill, QuillDeps

from prdprf.lessons.state import LessonAddPostFormState, LessonEditFormState, SelectTagState

modules = {
        'toolbar': [
            [{ 'header': [1, 2, False] }],
            ['bold', 'italic', 'underline','strike', 'blockquote'],
            [{'list': 'ordered'}, {'list': 'bullet'}, {'indent': '-1'}, {'indent': '+1'}],
            ['link', 'image'],
            ['formula'],
            ['clean'],
            ['video'],
            ['code-block'],
        ],

        'history': {
            'delay': 2000,
            'maxStack': 500,
            'userOnly': True,
        },

        'syntax': True, # TODO

        # TODO
        # 'clipboard': {},
}

formats = []


def blog_post_add_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    name="title",
                    placeholder="Заголовок",
                    required=True,
                    type='text',
                ),
                rx.spacer(),
                rx.select(
                    ["Математика", "Информатика", "Физика", "Робототехника", "Программирование"],
                    value=SelectTagState.value,
                    on_change=SelectTagState.change_value,
                    name='subject',
                ),
            ),
            *QuillDeps,
            ReactQuill.create(
                theme="snow",
                default_value=LessonAddPostFormState.content,
                on_change=LessonAddPostFormState.handle_change,
                modules=modules,
            ),
            rx.button("Опубликовать", type="submit"),
            align="center",
        ),
        on_submit=LessonAddPostFormState.handle_submit,
        reset_on_submit=True,
    )


def blog_post_edit_form() -> rx.Component:
    post = LessonEditFormState.post
    title = post.title
    content = post.content
    return rx.form(
        *QuillDeps,
        rx.box(
            rx.input(
                type='hidden',
                name='post_id',
                value=post.id
            ),
            display='none'
        ),
        rx.vstack(
            rx.hstack(
                rx.input(
                    default_value=title,
                    name="title",
                    placeholder="Название урока",
                    required=True,
                    type='text',
                    width='100%',
                ),
                width='100%'
            ),
            ReactQuill.create(
                theme="snow",
                default_value=content,
                on_change=LessonEditFormState.handle_change,
                modules=modules,
            ),
            rx.button("Опубликовать", type="submit"),
            align="center",
        ),
        on_submit=LessonEditFormState.handle_submit,
    )
