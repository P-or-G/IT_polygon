import reflex as rx

from prdprf.translator.state import RussianPythonTranslator
from prdprf.ui.base import base_page


def tab_button(tab_id: str, label: str, state_var: str) -> rx.Component:
    """Кастомная кнопка-вкладка."""
    return rx.button(
        label,
        on_click=lambda: RussianPythonTranslator.set_active_tab(tab_id),
        border_radius="md",
        padding_x="1.5em",
    )


def translator_page() -> rx.Component:
    return base_page(
        rx.container(
            rx.hstack(
                rx.vstack(
                    rx.button(
                        "Выполнить код",
                        on_click=RussianPythonTranslator.execute_code,
                        color_scheme="blue",
                    ),
                    rx.text_area(
                        id="code-input",
                        value=RussianPythonTranslator.russian_code,
                        on_change=RussianPythonTranslator.set_russian_code,
                        placeholder="Введите код на русском...",
                        height="100%",
                        width="100%",
                    ),
                    width="100%",
                    height="100%",
                ),
                rx.vstack(
                    # Кастомные вкладки без tab_list
                    rx.hstack(
                        tab_button("source", "Исходный код", RussianPythonTranslator.active_tab),
                        tab_button("result", "Результат", RussianPythonTranslator.active_tab),
                        spacing="1",
                        padding_bottom="0.5em",
                    ),
                    rx.box(
                        rx.cond(
                            RussianPythonTranslator.active_tab == "source",
                            rx.code_block(
                                RussianPythonTranslator.russian_code,
                                language="python",
                                width="100%",
                            ),
                        ),
                        rx.cond(
                            RussianPythonTranslator.active_tab == "result",
                            rx.vstack(
                                rx.text("Переведенный код:", font_weight="bold"),
                                rx.code_block(
                                    RussianPythonTranslator.translated_code,
                                    language="python",
                                    margin_bottom="1em",
                                ),
                                rx.divider(),
                                rx.text("Вывод программы:", font_weight="bold"),
                                rx.box(
                                    # Важное изменение здесь:
                                    rx.text(
                                        RussianPythonTranslator.execution_output,
                                        white_space="pre-wrap",  # Сохраняет переносы строк
                                        font_family="monospace",
                                        width="100%",
                                    ),
                                    border="1px solid #e2e8f0",
                                    padding="1em",
                                    border_radius="md",
                                    width="100%",
                                ),
                                align_items="start",
                            ),
                        ),
                        border="1px solid #e2e8f0",
                        border_radius="lg",
                        width="100%",
                        padding="1em",
                        height="100%"
                    ),
                    spacing="1",
                    width="100%",
                    max_width="800px",
                    height="100%"
                ),
                padding_top="2em",
                height="65vh",
            ),
            spacing='7em',
            height="100%"
        ),
        height="100%"
    )
