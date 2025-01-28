import reflex as rx

from prdprf.lessons.state import BlogAddPostFormState, BlogEditFormState, SelectTagState


def blog_post_add_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    name="title",
                    placeholder="Заголовок",
                    required=True,
                    type='text',
                    width='100%',
                ),
                rx.spacer(),
                rx.select(
                    ["Математика", "Информатика", "Физика", "Робототехника", "Программирование"],
                    value=SelectTagState.value,
                    on_change=SelectTagState.change_value,
                    name='tag',
                ),
                align="center",
                width='100%',

            ),
            rx.editor(
                width="1000px",
                lang="ru",
                set_contents=BlogAddPostFormState.content,
                set_options=rx.EditorOptions(
                    katex="katex", # Будет переделано Ваней
                    button_list=[
                        ["font", "fontSize", "formatBlock"],
                        ["fontColor", "hiliteColor"],
                        [
                            "bold",
                            "underline",
                            "italic",
                            "strike",
                            "subscript",
                            "superscript",
                        ],
                        ["removeFormat"],
                        "/",
                        ["outdent", "indent"],
                        ['align', 'horizontalRule', 'list', 'lineHeight'],
                        ['table', 'link', 'image', 'video'],
                        ['fullScreen', 'showBlocks', 'codeView'],
                        ['preview', 'print'],
                        ["math"],
                    ]
                ),
                on_change=BlogAddPostFormState.handle_change,
            ),
            rx.button("Опубликовать", type="submit"),
        ),
        on_submit=BlogAddPostFormState.handle_submit,
        reset_on_submit=True,
    )


def blog_post_edit_form() -> rx.Component:
    post = BlogEditFormState.post
    title = post.title
    content = post.content
    publish_active = post.publish_active
    post_content = BlogEditFormState.post_content
    return rx.form(
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
            rx.editor(
                width="1000px",
                lang="ru",
                set_contents=content,
                set_options=rx.EditorOptions(
                    katex={
                        "src": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
                        "css": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"
                    },
                    button_list=[
                        ["font", "fontSize", "formatBlock"],
                        ["fontColor", "hiliteColor"],
                        [
                            "bold",
                            "underline",
                            "italic",
                            "strike",
                            "subscript",
                            "superscript",
                        ],
                        ["removeFormat"],
                        "/",
                        ["outdent", "indent"],
                        ['align', 'horizontalRule', 'list', 'lineHeight'],
                        ['table', 'link', 'image', 'video'],
                        ['fullScreen', 'showBlocks', 'codeView'],
                        ['preview', 'print'],
                        ["math"],
                    ]
                ),
                on_change=BlogEditFormState.handle_change,
            ),
            rx.button("Опубликовать", type="submit"),
            align="center",
        ),
        on_submit=BlogEditFormState.handle_submit,
    )
