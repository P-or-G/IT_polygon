import asyncio
import datetime

import reflex as rx
import reflex_local_auth

import sqlmodel
from reflex.event import EventSpec
from reflex_local_auth import LocalUser
from sqlmodel import select

from prdprf.models import UserInfo
from prdprf.navigation.routes import LOGIN_ROUTE, REGISTER_ROUTE


class SessionState(reflex_local_auth.LocalAuthState):
    """
    Тебе не нужно знать, что тут происходит
    |
    |
    |
    Тут обрабатывается состояние сессии, а ещё отсюда получаем все данные по пользователю из UserInfo
    А ещё обрабатываем состояние пользователя (вошёл или нет), здесь же делаем некоторый logout
    Вся реальная муть с обработкой состояний сессии в reflex_local_auth.LocalAuthState
    !!!МОЖЕТ БЫТЬ НУЖНО БУДЕТ ДОБАВИТЬ ВОЗВРАЩЕНИЕ ДРУГИХ СТОЛБИКОВ!!!
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
        Мы возвращаем только имя, если не можем (сессия нужна), то None
        """
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username

    @rx.var(cache=True)
    def authenticated_user_info(self) -> UserInfo | None:
        """
        Мы возвращаем ВСЁ, что есть в UserInfo (дада, весь класс), если не можем (сессия нужна), то None
        """
        if self.authenticated_user.id < 0:
            return None
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(UserInfo).where(
                    UserInfo.user_id == self.authenticated_user.id
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


def redir():
    return rx.redirect(REGISTER_ROUTE)


class MyRegisterState(reflex_local_auth.LocalAuthState):

    success: bool = False
    error_message: str = ""
    new_user_id: int = -1

    def _validate_fields(
        self, username, password, confirm_password
    ) -> rx.event.EventSpec | list[rx.event.EventSpec] | None:
        if not username:
            self.error_message = "Поле Адрес не может быть пустым"
            return rx.set_focus("username")
        with rx.session() as session:
            existing_user = session.exec(
                select(UserInfo).where(UserInfo.username == username)
            ).one_or_none()
        if existing_user is not None:
            self.error_message = (
                f"Почта {username} уже зарегистрирована, попробуйте войти"
            )
            return [rx.set_value("username", ""), rx.set_focus("username")]
        if not password:
            self.error_message = "Поле Пароль не может быть пустым"
            return rx.set_focus("password")
        if password != confirm_password:
            self.error_message = "Пароли не совпадают"
            return [
                rx.set_value("confirm_password", ""),
                rx.set_focus("confirm_password"),
            ]

    def _register_user(self, form_data) -> None:
        with rx.session() as session:
            new_user = UserInfo(
                email=form_data["Адрес"],
                password_hash=UserInfo.hash_password(form_data["Пароль"]),
                enabled=True,
                username=form_data["Имя"],
                surname=form_data["Фамилия"],
                grade=form_data["grade"],
                litera=form_data["litera"],
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

        email = form_data["Адрес"]
        password = form_data["Пароль"]
        validation_errors = self._validate_fields(
            email, password, form_data["Подтверждение пароля"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(form_data)

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
            and password
            and user.verify(password)
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
