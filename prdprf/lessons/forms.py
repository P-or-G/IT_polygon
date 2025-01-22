import reflex as rx

from prdprf.lessons.state import BlogAddPostFormState, BlogEditFormState, EditorState


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
                width='100%'
            ),
            rx.editor(
                set_contents=EditorState.content,
                set_options=rx.EditorOptions(
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
                        ['save', 'template'],
                    ]
                ),
                on_change=EditorState.handle_change,
            ),
            rx.button("Сохранить", type="submit"),
        ),
        on_submit=BlogAddPostFormState.handle_submit,
        reset_on_submit=True,
    )


def blog_post_edit_form() -> rx.Component:
    post = BlogEditFormState.post
    title = post.title
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
                set_contents=EditorState.content,
                on_change=EditorState.handle_change,
            ),
            rx.box(
                rx.hstack(
                    rx.input(
                        default_value=BlogEditFormState.publish_display_date,
                        type='date',
                        name='publish_date',
                        width='100%'
                    ),
                    rx.input(
                        default_value=BlogEditFormState.publish_display_time,
                        type='time',
                        name='publish_time',
                        width='100%'
                    ),
                    width='100%'
                ),
                width='100%'
            ),
            rx.button("Опубликовать", type="submit"),
        ),
        on_submit=BlogEditFormState.handle_submit,
    )
