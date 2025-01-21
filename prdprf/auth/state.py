import reflex as rx
import reflex_local_auth

import sqlmodel
from reflex.event import EventSpec

from prdprf.models import UserInfo


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


class MyRegisterState(reflex_local_auth.RegistrationState):
    def handle_registration(self, form_data) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        """
        Тут проверяется регистрация, всё делается через reflex_local_auth модуль.
        Проверка идёт по паролю/подтверждению пароля и по уникальности юзернаме.
        Возвращает ID как будто Autoincrement в SQL (вообще, це единственное отличие от Родительского класса
        """
        username = form_data["Имя"]
        password = form_data["Пароль"]
        validation_errors = self._validate_fields(
            username, password, form_data["Подтверждение пароля"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return self.new_user_id
    
    def handle_registration_email(self, form_data):
        """
        Тут "дозаполняевывается" модуль UserInfo базы данных фамилией, почтой, классом и литерой
        """
        new_user_id = self.handle_registration(form_data)
        if new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["Адрес"],
                        user_id=self.new_user_id,
                        surname=form_data["Фамилия"],
                        grade=form_data["grade"],
                        litera=form_data["litera"],
                    )
                )
                session.commit()
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
