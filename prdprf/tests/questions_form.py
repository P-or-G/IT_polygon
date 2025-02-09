import reflex as rx
from typing import Dict, Any
from prdprf.models import Test, Question
from prdprf.tests.quest_state import QuestsState


def add_question_form():
    return rx.vstack(
        rx.heading("Создать задание"),
        rx.input(
            placeholder="Предмет вопроса",
            on_change=QuestsState.handle_subject_change,
            value=QuestsState.new_quest_subject,
        ),
        rx.text_area(
            placeholder="Вопрос",
            on_change=QuestsState.handle_text_change,
            value=QuestsState.new_quest_text,
        ),
        rx.input(
            placeholder="Тема теста",
            on_change=QuestsState.handle_answer_change,
            value=QuestsState.new_quest_answer,
        ),
        rx.input(
            placeholder="1",
            on_change=QuestsState.handle_score_change,
            value=QuestsState.new_quest_score,
        ),
        rx.cond(QuestsState.error_message, rx.text(QuestsState.error_message, color="red")),
        rx.button("Добавить тест", on_click=QuestsState.add_test)
    )
