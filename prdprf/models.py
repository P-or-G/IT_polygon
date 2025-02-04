from typing import Optional, List, Dict, Any
from datetime import datetime

import bcrypt
import reflex as rx
import reflex_local_auth
from reflex_local_auth.user import LocalUser

import sqlalchemy
from sqlalchemy import Column
from sqlmodel import Field, Relationship

from prdprf import utils



class UserInfo(rx.Model, table=True):
    user_id: int = Field(foreign_key='localuser.id', nullable=True)
    email: str = Field(unique=True, nullable=False, index=True)
    username: str
    surname: str

    password_hash: bytes = Field(nullable=False)
    enabled: bool = False

    grade: str
    litera: str
    points: int = 0

    teacher: bool = False

    com_lessons: dict = Field(default={}, sa_column=sqlalchemy.Column("com_lessons", sqlalchemy.JSON))
    posts: List['BlogPostModel'] = Relationship(
        back_populates='userinfo'
    )
    contact_entries: List['ContactEntryModel'] = Relationship(
        back_populates='userinfo'
    )

    @staticmethod
    def hash_password(secret: str) -> bytes:
        return bcrypt.hashpw(
            password=secret.encode("utf-8"),
            salt=bcrypt.gensalt(),
        )

    def verify(self, secret: str) -> bool:
        return bcrypt.checkpw(
            password=secret.encode("utf-8"),
            hashed_password=self.password_hash,
        )

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d.pop("password_hash", None)
        return d


class BlogPostModel(rx.Model, table=True):
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="posts")
    title: str
    content: str
    tags: dict = Field(default={}, sa_column=sqlalchemy.Column("tags", sqlalchemy.JSON))
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=True
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=True
    )
    publish_active: bool = True
    publish_date: datetime = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
    )


class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="contact_entries")
    first_name: str
    last_name: str | None = None
    email: str | None = None  # = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )


class LessonsModel(rx.Model, table=True):
    creator_id: int = Field(default=None, foreign_key="userinfo.id")
    ...
    questions: dict = Field(default={}, sa_column=sqlalchemy.Column("questions", sqlalchemy.JSON))
    ...

class Test(rx.Model, table=True):
    title: str | None = None # Название теста
    subject: str | None = None # Предмет теста
    json_data_as_string: str = ""  # JSON данные теста в виде строки

    @property  # Декоратор для создания свойства, позволяющего работать с JSON как со словарем
    def json_data(self) -> Dict[str, Any]:
        """Получить JSON данные в виде словаря."""
        try:
            return json.loads(self.json_data_as_string)  # Преобразование JSON строки в словарь Python
        except (json.JSONDecodeError, TypeError):  # Обработка ошибок преобразования JSON
            return {}  # Возврат пустого словаря, если произошла ошибка

    @json_data.setter  # Декоратор для установки JSON данных из словаря
    def json_data(self, value: Dict[str, Any]):
        """Установить JSON данные из словаря, сохранив строку."""
        try:
            self.json_data_as_string = json.dumps(value)  # Преобразование словаря Python в JSON строку
        except TypeError:
            self.json_data_as_string = ""  # Установка пустой строки, если преобразование не удалось

    def update_json_data(self, key: str, value: Any):
        """Обновить или добавить поле в json"""
        data = self.json_data  # Получение текущих JSON данных
        data[key] = value  # Обновление или добавление значения по ключу
        self.json_data = data  # Установка обновленных JSON данных


