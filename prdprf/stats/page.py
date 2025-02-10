import reflex as rx

from prdprf.models import UserInfo
from prdprf.stats.state import UsersTableState


def show_users(user: UserInfo):
    return rx.table.row(
        rx.table.cell(user.username),
        rx.table.cell(user.surname),
        rx.table.cell(user.grade),
        rx.table.cell(user.litera),
        rx.table.cell(user.points),
    )


def loading_data_table_example():
    return rx.vstack(
        # rx.select(
        #     ['Имя', 'Фамилия', 'Счёт'],
        #     placeholder="Sort By: Name",
        #     on_change=lambda value: UsersTableState.sort_values(
        #         value
        #     ),
        # ),
        # rx.input(
        #     placeholder="Search here...",
        #     on_change=lambda value: UsersTableState.filter_values(
        #         value
        #     ),
        # ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Имя"),
                    rx.table.column_header_cell("Фамилия"),
                    rx.table.column_header_cell("Класс"),
                    rx.table.column_header_cell("Литера"),
                    rx.table.column_header_cell("Рейтинг"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    UsersTableState.users, show_users
                )
            ),
            on_mount=UsersTableState.load_entries,
            width="100%",
        )
    )
