import reflex as rx
from sqlmodel import Field, SQLModel, create_engine, Session

POST_ID = 1
COLOR_SCHEME = {
    'Ученик':'green',
    'Учитель':'orange',
    'Системный администратор':'red'
}

# --- Модель бд для комментариев ---
class Comment(rx.Model, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    text: str
    post_id: int  # Привязка к посту

class Reply(rx.Model, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Уникальный ID
    username: str  # Имя пользователя, оставившего ответ
    text: str  # Текст ответа
    comment_id: int  # ID комментария, на который отвечают
    is_hiden: bool = Field(default=True)

# --- База данных ---
DATABASE_URL = "sqlite:///comments.db"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


# --- Состояние приложения ---
class CommentState(rx.State):
    comments: list[Comment] = []  # Список всех комментариев
    username: str = ""  # Текущий пользователь
    comment_text: str = ""  # Текст нового комментария

    dialog_name: str = ""
    comment_content: str = ""

    def load_comments(self):
        """Загрузить комментарии из базы данных для определённого поста."""
        with Session(engine) as session:
            self.comments = session.query(Comment).filter(Comment.post_id == POST_ID).all()

    def add_comment(self):
        """Добавить новый комментарий для определённого поста."""
        if self.dialog_name.strip() and self.comment_content.strip():
            new_comment = Comment(
                username=self.dialog_name,
                text=self.comment_content,
                post_id=POST_ID,  # Используем глобальную переменную
            )
            with Session(engine) as session:
                session.add(new_comment)
                session.commit()
            self.load_comments()  # Обновить список комментариев
            self.dialog_name = ""  # Очистить поля
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
    reply_username: str = ""  # Имя пользователя, оставляющего ответ
    reply_text: str = ""  # Текст ответа
    reply_comment_id: int | None = None  # ID комментария, на который отвечают
    replies: list[Reply] = []

    def show_replies(self, comment_id: int):
        with Session(engine) as session:
            replies = session.exec(
                Reply.select().where(
                    (Reply.comment_id == comment_id)
                )
            ).all()
            for reply in replies:
                reply.is_hiden = not reply.is_hiden
                session.add(reply)
                session.commit()
        self.load_replies()

    def set_reply_comment_id(self, comment_id: int):
        self.reply_comment_id = comment_id

    def add_reply(self, comment_id):
        self.reply_comment_id = comment_id
        """Добавить ответ на комментарий."""
        if self.reply_username.strip() and self.reply_text.strip() and self.reply_comment_id is not None:
            new_reply = Reply(
                username=self.reply_username,
                text=self.reply_text,
                comment_id=self.reply_comment_id,
            )
            with Session(engine) as session:
                session.add(new_reply)
                session.commit()
            self.show_replies(comment_id)
            self.reply_username = ""  # Очистить поля
            self.reply_text = ""  # Очистить текст ответа
            self.reply_comment_id = None  # Сбросить ID комментария
            self.load_replies()
            CommentState.load_comments()
            # Обновить список комментариев

    def load_replies(self):
        result = {}
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
                    rx.input(
                        placeholder="Введите ваше имя",
                        value=CommentState.dialog_name,
                        on_change=CommentState.set_dialog_name,
                        required=True,
                        size="3",
                        width="100%",
                        border_radius="md",
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
                    rx.input(
                        placeholder="Введите ваше имя",
                        value=ReplyState.reply_username,
                        on_change=ReplyState.set_reply_username,
                        required=True,
                        size="3",
                        width="100%",
                        border_radius="md",
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


# --- Главная страница ---
def index() -> rx.Component:
    CommentState.load_comments()
    ReplyState.load_replies()
    # Загрузить комментарии для текущего поста
    return rx.box(
        rx.vstack(
            add_customer_dialog(),  # Диалоговое окно для добавления комментария
            rx.divider(),
            rx.foreach(
                CommentState.comments,
                lambda comment: rx.vstack(
                    rx.hstack(
                        rx.icon(tag="user", size=20),
                        rx.text(f"{comment.username}", size="4", weight="bold"),
                        rx.code(f"Ученик", size="3", weight="bold", color_scheme=COLOR_SCHEME["Ученик"]), # ТУТ НЕ USERNAME ТУТ СТАТУС В ШКОЛЕ (УЧИТЕЛЬ/УЧЕНИК/СИС.АДМИН)
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
                            comment.username == 'Администратор', # ТУТ НЕ USERNAME ТУТ СТАТУС В ШКОЛЕ (УЧИТЕЛЬ/УЧЕНИК/СИС.АДМИН)
                            rx.button(
                                "Удалить",
                                color_scheme="red",
                                size="1",
                                on_click=lambda c_id=comment.id: CommentState.delete_comment(c_id),
                            ),
                            rx.box()
                        ),
                        justify="end",
                    ),
                    rx.foreach(
                        ReplyState.replies,
                        lambda reply: rx.cond(
                            (reply.comment_id == comment.id) & (~ reply.is_hiden),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(tag="user", size=16),
                                    rx.text(f"{reply.username}", size="3", weight="bold"),
                                    rx.code(f"Ученик", size="1", weight="bold", color_scheme=COLOR_SCHEME["Ученик"]), # ТУТ НЕ USERNAME ТУТ СТАТУС В ШКОЛЕ (УЧИТЕЛЬ/УЧЕНИК/СИС.АДМИН)
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
    )



# --- Приложение ---
app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Комментарии",
)