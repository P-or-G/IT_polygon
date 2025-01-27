import reflex as rx
from sqlmodel import Field, SQLModel, create_engine, Session


# --- Модель бд для комментариев ---
class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    text: str


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
        """Загрузить комментарии из базы данных."""
        with Session(engine) as session:
            self.comments = session.query(Comment).all()

    def add_comment(self):
        """Добавить новый комментарий из диалогового окна."""
        if self.dialog_name.strip() and self.comment_content.strip():
            new_comment = Comment(username=self.dialog_name, text=self.comment_content)
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
                    # Поле "Name"
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
                                    on_click=CommentState.add_comment,
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
    return rx.box(
        rx.vstack(
            add_customer_dialog(),  # Добавление диалогового окна
            rx.divider(),
            rx.foreach(
                CommentState.comments,
                lambda comment: rx.vstack(
                    rx.hstack(
                        # Иконка перед именем
                        rx.icon(tag="user", size=20),
                        rx.text(f"{comment.username}", size="4", weight="bold"),
                        justify="start",
                        spacing="2",
                    ),
                    # Текст комментария
                    rx.text(comment.text, size="3", margin_left="2rem"),
                    rx.hstack(
                        rx.button(
                            "🗑️",
                            color_scheme="red",
                            size="1",
                            on_click=lambda c_id=comment.id: CommentState.delete_comment(c_id),
                        ),
                        justify="end",
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
    title="Комментарии"
)
#всё в 1 файле
#чтобы удобно было интерпритировать сразу в проект
#потестирую
#то пойду делать ответы на комментарии оке оке понял #давай через