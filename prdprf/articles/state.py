from datetime import datetime
from typing import Optional, List
import reflex as rx 

import sqlalchemy
from sqlmodel import select

from prdprf import navigation
from prdprf.auth.state import SessionState
from prdprf.models import LessonPostModel, UserInfo

ARTICLE_LIST_ROUTE = navigation.routes.ARTICLE_LIST_ROUTE
if ARTICLE_LIST_ROUTE.endswith("/"):
    ARTICLE_LIST_ROUTE = ARTICLE_LIST_ROUTE[:-1]


class ArticlePublicState(SessionState):
    posts: List['LessonPostModel'] = []
    post: Optional['LessonPostModel'] = None
    post_content: str = ""
    post_publish_active: bool = True
    limit: int = 20

    @rx.var
    def post_id(self):
        return self.router.page.params.get("post_id", "")

    @rx.var
    def post_url(self):
        if not self.post:
            return f"{ARTICLE_LIST_ROUTE}"
        return f"{ARTICLE_LIST_ROUTE}/{self.post.id}"

    def get_post_detail(self):
        lookups = (
                (LessonPostModel.publish_active == True) &
                (LessonPostModel.publish_date < datetime.now()) &
                (LessonPostModel.id == self.post_id)
        )
        with rx.session() as session:
            if self.post_id == "":
                self.post = None
                self.post_content = ""
                self.post_publish_active = False
                return
            sql_statement = select(LessonPostModel).options(
                sqlalchemy.orm.joinedload(LessonPostModel.userinfo).joinedload(UserInfo.user)
            ).where(lookups)
            result = session.exec(sql_statement).one_or_none()
            self.post = result
            if result is None:
                self.post_content = ""
                return
            self.post_content = self.post.content
            self.post_publish_active = self.post.publish_active
        # return

    def set_limit_and_reload(self, new_limit: int=5):
        self.limit = new_limit
        self.load_posts()
        yield

    def load_posts(self, *args, **kwargs):

        with rx.session() as session:
            result = session.exec(
                select(LessonPostModel).options(sqlalchemy.orm.joinedload(LessonPostModel.userinfo))).all()
            self.posts = result
    
    def to_post(self):
        if not self.post:
            return rx.redirect(ARTICLE_LIST_ROUTE)
        return rx.redirect(f"{self.post_url}")
