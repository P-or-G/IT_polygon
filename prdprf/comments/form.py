import reflex as rx
from sqlmodel import select
from reflex_local_auth.auth_session import LocalAuthSession
from sqlmodel import Field, SQLModel, create_engine, Session

from prdprf.auth.state import SessionState, MyLocalAuthState
from prdprf.models import Comment, Reply, UserInfo

POST_ID = 1

class User():
    username = 'КрутойЧоч2007'

    firstname = 'Чоч'
    lastname = 'Чочевис'
    status = 'Системный администратор'


# --- Состояние приложения ---
class CommentState(rx.State):
    comments: list[Comment] = []  # Список всех комментариев
    comment_text: str = ""  # Текст нового комментария

    comment_content: str = ""

    def load_comments(self):
        """Загрузить комментарии из базы данных для определённого поста."""
        with rx.session() as session:
            self.comments = session.query(Comment).filter(Comment.post_id == POST_ID).all()

    def add_comment(self):
        """Добавить новый комментарий для определённого поста."""
        with rx.session() as session:
            user = session.exec(select(UserInfo).where(UserInfo.id == LocalAuthSession.user_id)).first()
            print(user)
        if self.comment_content.strip():
            new_comment = Comment(
                username=user.username,
                surname=user.surname,
                userstatus=user.teacher,
                text=self.comment_content,
                post_id=POST_ID,  # Используем глобальную переменную
            )
            with rx.session() as session:
                session.add(new_comment)
                session.commit()
            self.load_comments()  # Обновить список комментариев
            self.comment_content = ""  # Очистить текст комментария

    def delete_comment(self, comment_id: int):
        """Удалить комментарий."""
        with Session(engine) as session:
            comment = session.get(Comment, comment_id)
            if comment:
                session.delete(comment)
                session.commit()
        self.load_comments()  # Обновить список комментариев


class ReplyState(rx.State):
    reply_username: str = SessionState.authenticated_username
    reply_surname: str = SessionState.authenticated_surname
    userstatus: str = rx.cond(SessionState.authenticated_teacher, "Учитель", "Ученик")

    reply_text: str = ""  # Текст ответа
    reply_comment_id: int | None = None  # ID комментария, на который отвечают
    replies: list[Reply] = []

    def show_replies(self, comment_id: int, show_all=False):
        with Session(engine) as session:
            replies = session.exec(
                Reply.select().where(
                    (Reply.comment_id == comment_id)
                )
            ).all()
            for reply in replies:
                if show_all:
                    reply.is_hidden = False
                else:
                    reply.is_hidden = not reply.is_hidden
                session.add(reply)
                session.commit()
        self.load_replies()

    def set_reply_comment_id(self, comment_id: int):
        self.reply_comment_id = comment_id

    def add_reply(self, comment_id):
        self.reply_comment_id = comment_id
        """Добавить ответ на комментарий."""
        if self.reply_text.strip() and self.reply_comment_id is not None:
            new_reply = Reply(
                username=self.reply_username,
                userstatus=self.userstatus,
                text=self.reply_text,
                comment_id=self.reply_comment_id,
            )
            with Session(engine) as session:
                session.add(new_reply)
                session.commit()
            self.show_replies(comment_id, show_all=True)
            self.reply_text = ""  # Очистить текст ответа
            self.reply_comment_id = None  # Сбросить ID комментария
            self.load_replies()
            # Обновить список комментариев

    def load_replies(self):
        with Session(engine) as session:
            self.replies = session.query(Reply).all()


# --- Диалоговое окно ---
def add_customer_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Добавить комментарий",
                size="4",
                color_scheme="green",
            ),
        ),
        rx.dialog.content(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="text", size=24, margin_right="0.5rem"),
                        rx.dialog.title(
                            "Добавить комментарий",
                            weight="bold",
                            margin="0 0 1rem 0",
                            align="center",
                        ),
                    ),
                    rx.text_area(
                        placeholder="Введите текст комментария",
                        value=CommentState.comment_content,
                        on_change=CommentState.set_comment_content,
                        required=True,
                        size="3",
                        width="100%",
                        border_radius="md",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Отмена",
                                variant="soft",
                                color_scheme="gray",
                                size="4",
                                width="48%",
                                border_radius="md",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button(
                                    "Опубликовать",
                                    color_scheme="green",
                                    size="4",
                                    width="100%",
                                    border_radius="md",
                                    on_click=CommentState.add_comment,  # Используем глобальную переменную
                                ),
                            ),
                            as_child=True,
                        ),
                        justify="between",
                        width="100%",
                        margin_top="2rem",
                    ),
                    spacing="2",
                    width="100%",
                ),
                align="center",
                justify="center",
                width="100%",
                padding="2rem",
                direction="column",
            ),
            max_width="450px",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
            padding="1.5em",
        ),
    )


def reply_dialog(comment_id) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Ответить на комментарий",
                size="1",
                color_scheme="green",
            ),
        ),
        rx.dialog.content(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="text", size=24, margin_right="0.5rem"),
                        rx.dialog.title(
                            f"Ответить на комментарий",
                            weight="bold",
                            margin="0 0 1rem 0",
                            align="center",
                        ),
                    ),
                    rx.text_area(
                        placeholder="Введите текст ответа",
                        value=ReplyState.reply_text,
                        on_change=ReplyState.set_reply_text,
                        required=True,
                        size="3",
                        width="100%",
                        border_radius="md",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Отмена",
                                variant="soft",
                                color_scheme="gray",
                                size="4",
                                width="48%",
                                border_radius="md",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button(
                                    "Опубликовать",
                                    color_scheme="green",
                                    size="4",
                                    width="100%",
                                    border_radius="md",
                                    on_click=ReplyState.add_reply(comment_id),  # Используем глобальную переменную
                                ),
                            ),
                            as_child=True,
                        ),
                        justify="between",
                        width="100%",
                        margin_top="2rem",
                    ),
                    spacing="2",
                    width="100%",
                ),
                align="center",
                justify="center",
                width="100%",
                padding="2rem",
                direction="column",
            ),
            max_width="450px",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
            padding="1.5em",
        ),
    )


def confirm_action_dialog(comment):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Удалить",
                size="1",
                color_scheme="red",
            ),
        ),
        rx.dialog.content(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="user-round-check", size=24, margin_right="0.5rem"),
                        rx.dialog.title(
                            "Подтвердите своё действие",
                            weight="bold",
                            margin="0 0 1rem 0",
                            align="center",
                        ),
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Отмена",
                                variant="soft",
                                color_scheme="red",
                                size="4",
                                width="48%",
                                border_radius="md",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button(
                                    "Подтвердить",
                                    color_scheme="green",
                                    size="4",
                                    width="100%",
                                    border_radius="md",
                                    on_click=lambda c_id=comment.id: CommentState.delete_comment(c_id),  # Используем глобальную переменную
                                ),
                            ),
                            as_child=True,
                        ),
                        justify="between",
                        width="100%",
                        margin_top="2rem",
                    ),
                    spacing="1",
                    width="100%",
                ),
                align="center",
                justify="center",
                width="100%",
                padding="2rem",
                direction="column",
            ),
            max_width="450px",
            border=f"2px solid {rx.color('red', 7)}",
            border_radius="25px",
            padding="1.5em",

        ),
    )


# --- Главная страница ---
def index() -> rx.Component:
    CommentState.load_comments()
    ReplyState.load_replies()
    # Загрузить комментарии для текущего поста
    return rx.flex(
        rx.vstack(
            add_customer_dialog(),  # Диалоговое окно для добавления комментария
            rx.divider(),
            rx.foreach(
                CommentState.comments,
                lambda comment: rx.vstack(
                    rx.hstack(
                        rx.icon(tag="user", size=20),
                        rx.text(f"{comment.username}", size="4", weight="bold"),
                        rx.code(f"{comment.userstatus}", size="3", weight="bold", color_scheme='yellow'),
                        justify="start",
                        spacing="2",
                    ),
                    rx.text(comment.text, size="3", margin_left="2rem"),
                    rx.hstack(
                        reply_dialog(comment.id),
                        rx.button(
                            "Посмотреть ответы ▽",
                            color_scheme="gray",
                            size="1",
                            on_click=lambda c_id=comment.id: ReplyState.show_replies(c_id),
                        ),
                        rx.cond(
                            User.status == 'Системный администратор',
                            confirm_action_dialog(comment),
                            rx.box()
                        ),
                        justify="end",
                    ),
                    rx.foreach(
                        ReplyState.replies,
                        lambda reply: rx.cond(
                            (reply.comment_id == comment.id) & (~ reply.is_hidden),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(tag="user", size=16),
                                    rx.text(f"{reply.username}", size="3", weight="bold"),
                                    rx.code(f"{reply.userstatus}", size="3", weight="bold", color_scheme='yellow'),
                                    justify="start",
                                    spacing="2",
                                    margin_left="2rem",
                                ),
                                rx.text(reply.text, size="2", margin_left="4rem"),
                                spacing="1",
                                width="100%",
                            ),
                            rx.box()
                        )
                    ),
                    padding="1rem",
                    spacing="1",
                    width="100%",
                    border_bottom="1px solid #ddd",
                ),
            ),
            spacing="2",
            padding="1rem",
            align_items="flex-start",
        ),
        padding="2rem",
        width="1000px",
    )
