import reflex as rx
import reflex_local_auth
from reflex_local_auth.pages.components import input_100w, MIN_WIDTH
from .google_auth import login, require_google_login, CLIENT_ID, State
from .react_oauth_google import GoogleOAuthProvider, GoogleLogin

from prdprf.auth.state import MyRegisterState, SelectLiteraState, SelectClassState, redir, MyLoginState



def register_error() -> rx.Component:
    return rx.cond(
        reflex_local_auth.RegistrationState.error_message != "",
        rx.callout(
            reflex_local_auth.RegistrationState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )


def login_error() -> rx.Component:
    return rx.cond(
        MyLoginState.error_message != "",
        rx.callout(
            MyLoginState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )


def my_login_form() -> rx.Component:
    return GoogleOAuthProvider.create(rx.form(
        rx.vstack(
            rx.heading("Войдите в свой аккаунт", size="7"),
            login_error(),
            input_100w("Почта", type="example@choch.com"),
            input_100w("Пароль", type="12345678"),
            rx.button("Войти", width="100%"),
            rx.center(
                rx.link("Создать аккаунт", on_click=redir),
                width="100%",
            ),
            rx.center(
                GoogleLogin.create(on_success=MyLoginState.handle_google_login),
                width="100%",
            ),
            min_width=MIN_WIDTH,
        ),
        on_submit=MyLoginState.on_submit,
        ),
        client_id=CLIENT_ID,
    )


def my_register_form() -> rx.Component:
    return GoogleOAuthProvider.create(rx.form(
        rx.vstack(
            rx.heading("Создать аккаунт", size="7"),
            register_error(),
            input_100w("Имя", type='username'),
            input_100w("Фамилия", type='surname'),
            rx.hstack(
                rx.text("Класс обучения"),
                rx.select(
                    ["7", "8", "9", "10", "11",],
                    value=SelectClassState.value,
                    on_change=SelectClassState.change_value,
                    name='grade'
                ),
                rx.text("Буква"),
                rx.select(
                    ["А", "Б", "В", "Г", "Д", "Е", "М",],
                    value=SelectLiteraState.value,
                    on_change=SelectLiteraState.change_value,
                    name='litera',
                ),
            ),
            input_100w("Почта", type='email'),
            input_100w("Пароль", type="password"),
            input_100w("Подтверждение пароля", type="confirm_password"),
            rx.button("Зарегистрироваться", width="100%"),
            rx.center(
                rx.link(
                    "Войти в существующий аккаунт",
                    on_click=lambda: rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)),
                width="100%",
            ),
            rx.center(
                GoogleLogin.create(on_success=MyRegisterState.handle_google_reg),
                width="100%",
            ),
            min_width=MIN_WIDTH,
        ),
        on_submit=MyRegisterState.handle_registration,
        ),
        client_id=CLIENT_ID,
    )
