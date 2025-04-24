from datetime import datetime
from typing import Optional, List
import reflex as rx

import sqlalchemy
from sqlmodel import select

from prdprf import navigation
from prdprf.auth.state import SessionState
from prdprf.models import LessonPostModel, UserInfo

BLOG_POSTS_ROUTE = navigation.routes.LESSONS_ROUTE
if BLOG_POSTS_ROUTE.endswith("/"):
    BLOG_POSTS_ROUTE = BLOG_POSTS_ROUTE[:-1]


class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    @rx.event
    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    @rx.event
    def get_content(self):
        # You can process self.content here
        return self.content


class LessonPostState(SessionState):
    posts: List['LessonPostModel'] = []
    post: Optional['LessonPostModel'] = None
    post_content: str = ""
    post_publish_active: bool = True

    def class_name(self):
        return str(rx.color_mode_cond("blck", "wht")).split()[-3]

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get("blog_id", "")

    @rx.var
    def blog_post_url(self):
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}"

    @rx.var
    def blog_post_edit_url(self):
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}/edit"

    def get_post_detail(self):
        if self.my_userinfo_id is None:
            self.post = None
            self.post_content = ""
            self.post_publish_active = False
            return
        lookups = (
                (LessonPostModel.userinfo_id == self.my_userinfo_id) &
                (LessonPostModel.id == self.blog_post_id)
        )
        with rx.session() as session:
            if self.blog_post_id == "":
                self.post = None
                return
            sql_statement = select(LessonPostModel).options(
                sqlalchemy.orm.joinedload(LessonPostModel.userinfo)
            ).where(lookups)
            result = session.exec(sql_statement).one_or_none()
            self.post = result
            if result is None:
                self.post_content = ""
                return
            self.post_content = self.post.content
            self.post_publish_active = self.post.publish_active

    def load_posts(self, *args, **kwargs):
        with rx.session() as session:
            result = session.exec(
                select(LessonPostModel).options(
                    sqlalchemy.orm.joinedload(LessonPostModel.userinfo)
                ).where(LessonPostModel.userinfo_id == self.my_userinfo_id)
            ).all()
            self.posts = result
        # return

    def add_post(self, form_data: dict):
        with rx.session() as session:
            post = LessonPostModel(**form_data)
            session.add(post)
            session.commit()
            session.refresh(post)
            self.post = post

    def save_post_edits(self, post_id: int, updated_data: dict):
        with rx.session() as session:
            post = session.exec(
                select(LessonPostModel).where(
                    LessonPostModel.id == post_id
                )
            ).one_or_none()
            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value)
            session.add(post)
            session.commit()
            session.refresh(post)
            self.post = post

    def to_blog_post(self, edit_page=False):
        if not self.post:
            return rx.redirect(BLOG_POSTS_ROUTE)
        if edit_page:
            return rx.redirect(f"{self.blog_post_edit_url}")
        return rx.redirect(f"{self.blog_post_url}")


class LessonAddPostFormState(LessonPostState):
    form_data: dict = {}
    content: str = "<p>Содержание урока</p>"

    @rx.event
    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    def handle_submit(self, form_data):
        print(form_data)
        data = form_data.copy()
        data["content"] = self.content
        if self.my_userinfo_id is not None:
            data['userinfo_id'] = self.my_userinfo_id
        self.form_data = {**data, 'publish_active': True, 'publish_date': None}
        self.add_post(data)
        self.content = "<p>Содержание урока</p>"
        return self.to_blog_post()


class LessonEditFormState(LessonPostState):
    form_data: dict = {}
    content: str = "<p>Содержание урока</p>"

    @rx.event
    def handle_change(self, content: str):
        """Обновляет отображение"""
        self.content = content

    def handle_submit(self, form_data):
        self.form_data = form_data
        self.form_data["content"] = self.content
        post_id = form_data.pop('post_id')
        updated_data = {**form_data, 'publish_active': True, 'publish_date': None}
        self.save_post_edits(post_id, updated_data)
        self.content = "<p>Содержание урока</p>"
        return self.to_blog_post()


class SelectTagState(rx.State):
    """
    Собственно, обработка состояний select окошка для номера класса
    """
    value: str = "Математика"

    @rx.event
    def change_value(self, value: str):
        """
        !!!Осторожно, слишком сложная структура!!!
        Заменяет значение по ивенту для rx.select структур
        """
        self.value = value
