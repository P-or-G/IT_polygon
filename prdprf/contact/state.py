from typing import List
import asyncio
import reflex as rx 

from sqlmodel import select

from prdprf.auth.state import SessionState
from prdprf.models import ContactEntryModel


class ContactState(SessionState):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []
    did_submit: bool = False

    async def handle_submit(self, form_data: dict):
        """Хэндлер для отправки запроса, какие мы плохие"""
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        if self.my_user_id is not None:
            data['user_id'] = self.my_user_id
        if self.my_userinfo_id is not None:
            data['userinfo_id'] = self.my_userinfo_id
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries = entries