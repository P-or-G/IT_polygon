import reflex as rx

from prdprf.tasks_new.state import QuestionState, QuestionGeneratorState
from prdprf.ui.base import base_page


def test_page() -> rx.Component:
    return base_page(
        rx.cond(
            QuestionState.current_question.question_text,  # Проверяем, что вопрос загружен
            rx.vstack(
                rx.text(QuestionState.current_question.question_text),
                rx.input(
                    placeholder="Ваш ответ",
                    on_change=QuestionState.set_user_answer,
                ),
                rx.button(
                    "Ответить",
                    on_click=QuestionState.check_answer,
                ),
                rx.text(f"Баллы: {QuestionState.score}"),
            ),
            rx.text("Тест завершён!"),
        )
    )


def question_generator_form() -> rx.Component:
    return base_page(
        rx.vstack(
            # Поля для основного содержания вопроса
            rx.input(
                placeholder="Текст вопроса",
                on_change=QuestionGeneratorState.set_question_text,
                value=QuestionGeneratorState.question_text,
            ),
            rx.select(
                ["easy", "medium", "hard"],
                placeholder="Сложность",
                value=QuestionGeneratorState.difficulty,
                on_change=QuestionGeneratorState.set_difficulty,
            ),
            rx.input(
                placeholder="Тема вопроса",
                value=QuestionGeneratorState.topic,
                on_change=QuestionGeneratorState.set_topic,
            ),
            rx.divider(),

            # Список вариантов ответов
            rx.heading("Варианты ответов", size="5"),
            rx.foreach(
                QuestionGeneratorState.answers,
                lambda answer, idx: rx.hstack(
                    rx.checkbox(
                        is_checked=QuestionGeneratorState.correct_answers.contains(idx),
                        on_change=lambda: QuestionGeneratorState.toggle_correct_answer(idx)
                    ),
                    rx.input(
                        value=answer,
                        on_change=lambda value: QuestionGeneratorState.update_answer(idx, value),
                    ),
                    rx.button(
                        "×",
                        on_click=lambda: QuestionGeneratorState.remove_answer_field(idx),
                        color_scheme="red",
                        is_disabled=QuestionGeneratorState.answers.length() <= 2,
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            # Кнопки управления
            rx.button(
                "Добавить вариант",
                on_click=QuestionGeneratorState.add_answer_field,
            ),
            rx.button(
                "Сохранить вопрос",
                on_click=QuestionGeneratorState.save_question,
                color_scheme="green",
                is_disabled=rx.cond(
                    (QuestionGeneratorState.question_text.to(str).strip() == "") |
                    (QuestionGeneratorState.correct_answers.length() == 0),
                    True,
                    False
                )
            ),
            spacing="3",
        )
    )
