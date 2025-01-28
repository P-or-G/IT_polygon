from datetime import datetime

import reflex as rx
from reflex_global_hotkey import GlobalHotkeyWatcher
from reflex_local_auth.auth_session import LocalAuthSession
from sqlmodel import select

from prdprf.auth.state import MyLocalAuthState, SessionState
from prdprf.models import UserInfo


class StatusButtonState(rx.State):
    value: bool = ""

    @rx.event
    def update_key(self):
        with rx.session() as session:
            print(UserInfo.id, LocalAuthSession.user_id)
            user = session.exec(
                select(UserInfo).where(
                    UserInfo.id == LocalAuthSession.user_id,
                ),
            ).first()
            print(user)
            new_user = UserInfo(
                id=user.id,
                email=user.email,
                password_hash=user.password_hash,
                enabled=True,
                username=user.username,
                surname=user.surname,
                grade=user.grade,
                litera=user.litera,
                teacher=(not user.teacher)
            )
            self.value = not user.teacher
            session.delete(user)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

