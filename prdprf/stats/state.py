import reflex as rx
from sqlmodel import select, asc, or_, and_

from prdprf.models import UserInfo


class UsersTableState(rx.State):
    users: list[UserInfo] = []

    sort_value = ""
    search_value = ""
    grade_value = ""
    litera_value = ""

    @rx.event
    def load_entries(self):
        with rx.session() as session:
            query = select(UserInfo)

            if self.search_value != "" or (self.grade_value != "" and self.litera_value != ""):
                search_value = (
                    f"%{self.search_value.lower()}%"
                )
                grade_value = (
                    f"%{self.grade_value.lower()}%"
                )
                litera_value = (
                    f"%{self.litera_value.lower()}%"
                )
                query = query.where(
                    or_(
                        UserInfo.username.ilike(search_value),
                        UserInfo.surname.ilike(search_value),
                        and_(
                            UserInfo.grade.ilike(grade_value),
                            UserInfo.litera.ilike(litera_value)
                        )
                    )
                )

            self.users = session.exec(query.where(UserInfo.teacher == False)).all()

    @rx.event
    def sort_values(self, sort_value):
        self.sort_value = sort_value
        self.load_entries()

    @rx.event
    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()