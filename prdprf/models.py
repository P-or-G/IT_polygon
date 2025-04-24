from typing import Optional, List, Dict, Any
from datetime import datetime

import bcrypt
import reflex as rx

import sqlalchemy
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
    posts: List['LessonPostModel'] = Relationship(
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


class LessonPostModel(rx.Model, table=True):
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="posts")
    title: str
    content: str
    subject: str
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


class TestQuestionLink(rx.Model, table=True):
    test_id: int = Field(foreign_key="testmodel.id", primary_key=True)
    question_id: int = Field(foreign_key="question.id", primary_key=True)
    order: int = 0  # Порядок вопроса в тесте (опционально)


class Question(rx.Model, table=True):
    subject: str
    question_text: str
    answer: str
    score: int = 1

    # Связь с тестами
    tests: List["TestModel"] = Relationship(
        back_populates="questions",
        link_model=TestQuestionLink
    )


class TestModel(rx.Model, table=True):
    title: str = ""
    subject: str = ""
    description: str = ""
    time_limit: int = 0  # В секундах
    creator_id: int = Field(foreign_key="userinfo.id")

    # Связь с вопросами через промежуточную таблицу
    questions: List["Question"] = Relationship(
        back_populates="tests",
        link_model=TestQuestionLink  # Указываем связующую таблицу
    )
