import reflex as rx

import functools
import json
import os
import time

from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

from .react_oauth_google import (
    GoogleOAuthProvider,
    GoogleLogin,
)

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "268292277839-jj61fehiv0uc3laf9u2a069vvq4us1sd.apps.googleusercontent.com")
# CLIENT_ID = "XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.apps.googleusercontent.com"

class State(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    def reg_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    def login_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)


    @rx.var(cache=True)
    def tokeninfo(self) -> dict[str, str]:
        try:
            return verify_oauth2_token(
                json.loads(self.id_token_json)[
                    "credential"
                ],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: {exc}")

        return {}

    def logout(self):
        self.id_token_json = ""

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False

    @rx.var(cache=True)
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you {self.tokeninfo['name']}"
        return "Not logged in."


def login() -> rx.Component:
    return rx.vstack(
        GoogleLogin.create(on_success=State.on_success),
    )


def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                State.is_hydrated,
                rx.cond(
                    State.token_is_valid,
                    page(),
                    login()
                ),

                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )

    return _auth_wrapper