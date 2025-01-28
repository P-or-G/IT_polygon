from typing import Optional, List
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
