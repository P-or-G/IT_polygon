import reflex as rx
from prdprf.tests.quest_state import QuestsState


def add_question_form():
    return rx.center(
        rx.vstack(
            rx.heading("Создать задание"),
            rx.hstack(
                rx.select(
                    ["Математика", "Информатика", "Физика", "Робототехника", "Программирование"],
                    value=QuestsState.new_quest_subject,
                    on_change=QuestsState.handle_subject_change,
                    position="popper",
                ),
                rx.input(
                    placeholder="Ответ",
                    on_change=QuestsState.handle_answer_change,
                    value=QuestsState.new_quest_answer,
                    width="45%",
                    required=True
                ),
                rx.input(
                    placeholder="Баллы",
                    on_change=QuestsState.handle_score_change,
                    value=QuestsState.new_quest_score,
                    width="15%",
                    required=True
                ),
            ),
            rx.text_area(
                placeholder="Вопрос",
                on_change=QuestsState.handle_text_change,
                value=QuestsState.new_quest_text,
                width="1000px",
                required=True,
                resize="vertical",
            ),
            rx.cond(QuestsState.error_message, rx.text(QuestsState.error_message, color="red")),
            rx.button("Добавить тест", on_click=QuestsState.add_test),
            align='center'
        ),
    )
