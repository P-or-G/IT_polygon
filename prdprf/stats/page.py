import reflex as rx
from reflex import select

from prdprf.models import UserInfo


class UsersTableState(rx.State):
    users: list[UserInfo] = []

    @rx.event
    def load_entries(self):
        with rx.session() as session:
            self.users = session.exec(select(UserInfo)).all()


def create_table():
    return rx.flex(
        rx.heading("Статистика"),
        rx.text("Invite and manage your team members"),
        rx.flex(
            rx.input(placeholder="Email Address"),
            rx.button("Invite"),
            justify="center",
            spacing="2",
        ),
        rx.table.root(
            rx.table.body(
                rx.table.row(
                    rx.table.cell(rx.avatar(fallback="DS")),
                    rx.table.row_header_cell(
                        rx.link("Danilo Sousa")
                    ),
                    rx.table.cell("danilo@example.com"),
                    rx.table.cell("Developer"),
                    align="center",
                ),
                rx.table.row(
                    rx.table.cell(rx.avatar(fallback="ZA")),
                    rx.table.row_header_cell(
                        rx.link("Zahra Ambessa")
                    ),
                    rx.table.cell("zahra@example.com"),
                    rx.table.cell("Admin"),
                    align="center",
                ),
                rx.table.row(
                    rx.table.cell(rx.avatar(fallback="JE")),
                    rx.table.row_header_cell(
                        rx.link("Jasper Eriksson")
                    ),
                    rx.table.cell("jasper@example.com"),
                    rx.table.cell("Developer"),
                    align="center",
                ),
            ),
            width="100%",
        ),
        width="100%",
        direction="column",
        spacing="2",
    )
