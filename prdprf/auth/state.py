import asyncio
import datetime
import json
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

import reflex as rx
import reflex_local_auth

import sqlmodel
from reflex.event import EventSpec
from reflex_local_auth.auth_session import LocalAuthSession
from sqlmodel import select

from .google_auth import CLIENT_ID

from prdprf.models import UserInfo
from prdprf.navigation.routes import LOGIN_ROUTE, REGISTER_ROUTE


def redir():
    return rx.redirect(REGISTER_ROUTE)


class MyRegisterState(reflex_local_auth.LocalAuthState):
    success: bool = False
    error_message: str = ""
    new_user_id: int = -1

    def _validate_fields(
        self, email, password, confirm_password, token=None
    ) -> rx.event.EventSpec | list[rx.event.EventSpec] | None:
        if not email:
            self.error_message = "Поле Адрес не может быть пустым"
            return rx.set_focus("username")
        with rx.session() as session:
            existing_user = session.exec(
                select(UserInfo).where(UserInfo.email == email)
            ).one_or_none()
        if existing_user is not None:
            self.error_message = (
                f"Почта {email} уже зарегистрирована, попробуйте войти"
            )
            return [rx.set_value("username", ""), rx.set_focus("username")]
        if not password and not token:
            self.error_message = "Поле Пароль не может быть пустым"
            return rx.set_focus("password")
        if password and password != confirm_password:
            self.error_message = "Пароли не совпадают"
            return [
                rx.set_value("confirm_password", ""),
                rx.set_focus("confirm_password"),
            ]

    def _register_user(self, form_data) -> None:
        with rx.session() as session:
            new_user = UserInfo(
                password_hash=(None if (form_data["token"]) else UserInfo.hash_password(form_data["Пароль"])),
                email=form_data["Почта"],
                enabled=True,
                username=form_data["Имя"],
                surname=form_data["Фамилия"],
                grade=form_data["grade"],
                litera=form_data["litera"],
                token=form_data["token"],
            )  # type: ignore

            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            statement = select(UserInfo).where(UserInfo.id == new_user.id)
            results = session.exec(statement)
            us = results.one()
            us.user_id = new_user.id

            session.add(us)
            session.commit()
            session.refresh(us)

            self.new_user_id = new_user.id

    async def successful_registration(self):
        # Set success and redirect to login page after a brief delay.
        self.error_message = ""
        self.new_user_id = -1
        self.success = True
        yield
        await asyncio.sleep(0.5)
        yield [rx.redirect(LOGIN_ROUTE), MyRegisterState.set_success(False)]


    def handle_registration(self, form_data) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        """
        Тут проверяется регистрация, всё делается через reflex_local_auth модуль.
        Проверка идёт по паролю/подтверждению пароля и по уникальности юзернаме.
        Возвращает ID как будто Autoincrement в SQL (вообще, це единственное отличие от Родительского класса
        """

        email = form_data["Почта"]

        try:
            password = form_data["Пароль"]
        except Exception:
            password = None

        try:
            token = form_data["token"]
        except Exception:
            token = None

        try:
            pc = form_data["Подтверждение пароля"]
        except Exception:
            pc = None
        validation_errors = self._validate_fields(
            email, password, pc, token
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(form_data)

        return type(self).successful_registration

    def handle_google_reg(self, token_id):
        try:
            token_info = verify_oauth2_token(
                token_id["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception:
            return {}

        self.handle_registration({
            "Имя": token_info["name"],
            "Фамилия": "", # у гугла можно поменять scopes и просить фамилию в принципе
            "Почта": token_info["email"],
            "token": token_info,
            "grade": 7,
            "litera": "А",
        })

        if self.new_user_id != -1:
            return type(self).successful_registration



class SelectClassState(rx.State):
    """
    Собственно, обработка состояний select окошка для номера класса
    """
    value: str = "7"

    @rx.event
    def change_value(self, value: str):
        """
        !!!Осторожно, слишком сложная структура!!!
        Заменяет значение по ивенту для rx.select структур
        """
        self.value = value


class SelectLiteraState(rx.State):
    """
    Собственно, обработка состояний select окошка для буквы класса
    """
    value: str = "А"

    @rx.event
    def change_value(self, value: str):
        """
        !!!Осторожно, слишком сложная структура!!!
        Заменяет значение по ивенту для rx.select структур
        """
        self.value = value


class MyLoginState(reflex_local_auth.LoginState):
    def on_submit(self, form_data) -> rx.event.EventSpec:
        self.error_message = ""
        email = form_data["Почта"]
        password = form_data["Пароль"]

        try:
            token = form_data["token"]
        except Exception:
            token = None

        with rx.session() as session:
            user = session.exec(
                select(UserInfo).where(UserInfo.email == email)
            ).one_or_none()

        if user is not None and not user.enabled:
            self.error_message = "Ваш аккаунт заблокирован"
            return rx.set_value("Пароль", "")

        if (
            user is not None
            and user.id is not None
            and user.enabled
            # and password
            # and user.verify(password)
        ):
            # mark the user as logged in
            self._login(user.id)
        else:
            self.error_message = "Что-то пошло не так"
            return rx.set_value("Пароль", "")

        self.error_message = ""
        self.is_hydrated = True
        self.is_authenticated = True

        return self.redir()

    def handle_google_login(self, token_id: dict):
        try:
            token_info = verify_oauth2_token(
                token_id["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception:
            return {}

        print(token_info)

        return self.on_submit({
            "Пароль": json.dumps(token_id),
            "Почта": token_info["email"],
        })



AUTH_TOKEN_LOCAL_STORAGE_KEY = "_auth_token"
DEFAULT_AUTH_SESSION_EXPIRATION_DELTA = datetime.timedelta(days=7)
DEFAULT_AUTH_REFRESH_DELTA = datetime.timedelta(minutes=10)


class MyLocalAuthState(rx.State):
    auth_token: str = rx.LocalStorage(name=AUTH_TOKEN_LOCAL_STORAGE_KEY)
    status: bool = False

    @rx.var(cache=True, interval=DEFAULT_AUTH_REFRESH_DELTA)
    def authenticated_user(self) -> UserInfo:

        with rx.session() as session:
            result = session.exec(
                select(UserInfo, LocalAuthSession).where(
                    LocalAuthSession.session_id == self.auth_token,
                    LocalAuthSession.expiration
                    >= datetime.datetime.now(datetime.timezone.utc),
                    UserInfo.id == LocalAuthSession.user_id,
                ),
            ).first()
            if result:
                user, session = result
                return user
        return UserInfo(id=-1)

    def get_user(self):
        with rx.session() as session:
            result = session.exec(
                select(UserInfo).where(
                    LocalAuthSession.session_id == self.auth_token,
                    LocalAuthSession.expiration
                    >= datetime.datetime.now(datetime.timezone.utc),
                    UserInfo.id == LocalAuthSession.user_id,
                ),
            ).first()
        return result

    @rx.var(cache=True, interval=DEFAULT_AUTH_REFRESH_DELTA)
    def is_authenticated(self) -> bool:
        return self.authenticated_user.id >= 0

    def do_logout(self) -> None:
        with rx.session() as session:
            for auth_session in session.exec(
                select(LocalAuthSession).where(LocalAuthSession.session_id == self.auth_token)
            ).all():
                session.delete(auth_session)
            session.commit()
        self.auth_token = self.auth_token

    def _login(
        self,
        user_id: int,
        expiration_delta: datetime.timedelta = DEFAULT_AUTH_SESSION_EXPIRATION_DELTA,
    ) -> None:
        self.do_logout()
        if user_id < 0:
            return
        self.auth_token = self.auth_token or self.router.session.client_token
        with rx.session() as session:
            session.add(
                LocalAuthSession(  # type: ignore
                    user_id=user_id,
                    session_id=self.auth_token,
                    expiration=datetime.datetime.now(datetime.timezone.utc)
                    + expiration_delta,
                )
            )
            session.commit()

    def status_change(self):
        with rx.session() as session:
            user = session.exec(
                select(UserInfo).where(
                    UserInfo.id == LocalAuthSession.user_id,
                ),
            ).first()
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
            self.status = not user.teacher
            session.delete(user)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

    @rx.event
    def update_value(self):
        with rx.session() as session:
            user = session.exec(select(UserInfo).where(UserInfo.id == LocalAuthSession.user_id)).first()
            self.status = user.teacher


class SessionState(MyLocalAuthState):
    """
    Тебе не нужно знать, что тут происходит
    |
    |
    |
    Тут обрабатывается состояние сессии, а ещё отсюда получаем все данные по пользователю из UserInfo
    А ещё обрабатываем состояние пользователя (вошёл или нет), здесь же делаем некоторый logout
    Вся реальная муть с обработкой состояний сессии в reflex_local_auth.LocalAuthState
    """

    @rx.var(cache=True)
    def my_userinfo_id(self) -> str | None:
        return self.authenticated_user_info.id

    @rx.var(cache=True)
    def my_user_id(self) -> str | None:
        """
        Если id больше или 0, оно скажет id, а меньше нуля тебе зачем?
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.id

    @rx.var(cache=True)
    def authenticated_username(self) -> str | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username

    @rx.var(cache=True)
    def authenticated_surname(self) -> str | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.surname

    @rx.var(cache=True)
    def authenticated_grade(self) -> str | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.grade

    @rx.var(cache=True)
    def authenticated_litera(self) -> str | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.litera

    @rx.var(cache=True)
    def authenticated_points(self) -> str | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.points

    @rx.var(cache=True)
    def authenticated_teacher(self) -> bool | None:
        """
        Мы возвращаем только имя, если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.teacher

    @rx.var(cache=True)
    def authenticated_user_info(self) -> UserInfo | None:
        """
        Мы возвращаем ВСЁ, что есть в UserInfo (весь класс), если не можем, то None
        """
        if self.authenticated_user.id < 0:
            return None
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(UserInfo).where(
                    UserInfo.id == self.authenticated_user.id
                ),
            ).one_or_none()
            if result is None:
                return None
            return result

    def on_load(self):
        """
        Проверяет зарегистрирован ли пользователь, если нет, то возвращает ивент редиректа на /
        Кроме случаев, когда мы на /login
        """
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.is_authenticated)
        print(self.authenticated_user_info)

    def perform_logout(self) -> EventSpec:
        """
        Обычный do_logout, но мы делаем редирект в итоге
        """
        self.do_logout()
        return rx.redirect("/")
