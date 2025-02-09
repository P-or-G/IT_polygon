import reflex as rx
import json
from typing import Dict, Any
from prdprf.models import Test

# Константы
INVALID_JSON_ERROR = "Некорректный JSON формат"
TEST_NOT_SELECTED = "Тест не выбран"
LOAD_TEST_ERROR = "Ошибка загрузки данных теста"
NO_TESTS_IN_DATABASE = "База данных пуста, добавлены примеры"


# Класс State для управления состоянием приложения
class TestsState(rx.State):
    tests: list[Test] = []  # Список тестов, загруженных из базы данных
    selected_test: Test = None  # Выбранный тест для просмотра деталей
    new_test_title: str = ""  # Название нового теста
    new_test_subject: str = ""  # Предмет нового теста
    new_test_topic = ""  # Сброс JSON данных нового теста
    new_test_text = ""  # Сброс JSON данных нового теста
    error_message: str = ""  # Сообщение об ошибке

    def on_mount(self):
        """Вызывается при монтировании страницы, загружает данные и если их нет, то добавляет тестовые данные"""
        self.fetch_tests()  # Загрузка тестов из базы данных
        with rx.session() as session:  # Создание сессии для работы с базой данных
            if not session.query(Test).first():  # Проверка, есть ли тесты в базе данных
                self.load_and_add_json()  # Загрузка и добавление тестовых данных
            else:
                self.error_message = NO_TESTS_IN_DATABASE  # Показать сообщение, что добавлены примеры

    def fetch_tests(self):
        """Загрузка всех тестов из базы данных"""
        with rx.session() as session:  # Создание сессии для работы с базой данных
            self.tests = session.query(Test).all()  # Запрос всех тестов

    def select_test(self, test: Test):
        """Выбор теста для просмотра деталей"""
        self.selected_test = test  # Установка выбранного теста

    def clear_selected_test(self):
        """Сброс выбора теста"""
        self.selected_test = None  # Сброс выбранного теста

    def handle_title_change(self, title):
        """Обработчик изменения названия нового теста"""
        self.new_test_title = title  # Обновление названия нового теста

    def handle_subject_change(self, subject):
        """Обработчик изменения предмета нового теста"""
        self.new_test_subject = subject  # Обновление предмета нового теста

    def handle_topic_change(self, topic):
        """Обработчик изменения предмета нового теста"""
        self.new_test_topic = topic  # Обновление предмета нового теста

    def handle_text_change(self, text):
        """Обработчик изменения предмета нового теста"""
        self.new_test_text = text  # Обновление предмета нового теста


    def add_test(self):
        """Добавление нового теста в базу данных"""


        with rx.session() as session:  # Создание сессии для работы с базой данных
            new_test = Test(title=self.new_test_title, subject=self.new_test_subject, topic=self.new_test_topic)  # Создание объекта Test
            new_test.test_text = self.new_test_text
            session.add(new_test)  # Добавление теста в базу данных
            session.commit()  # Сохранение изменений

        self.error_message = ""  # Сброс сообщения об ошибке
        self.new_test_title = ""  # Сброс названия нового теста
        self.new_test_subject = ""  # Сброс предмета нового теста
        self.new_test_topic = ""  # Сброс JSON данных нового теста
        self.new_test_text = ""  # Сброс JSON данных нового теста
        self.fetch_tests()  # Обновление списка тестов

def test_text_all():
    """Возвращает текст с предметом текущего теста"""
    return rx.text(f"{TestsState.selected_test.test_text}")

def subject_text():
    """Возвращает текст с предметом текущего теста"""
    return rx.text(f"Предмет: {TestsState.selected_test.subject}")


def topic_text():
    """Возвращает текст с предметом текущего теста"""
    return rx.text(f"Тема: {TestsState.selected_test.topic}")

# Функция для создания компонента списка тестов
def test_list():
    return rx.vstack(  # Вертикальное расположение компонентов
        rx.heading("Список тестов"),  # Заголовок списка тестов
        rx.button("Обновить", on_click=TestsState.fetch_tests),  # Кнопка для обновления списка тестов
        rx.list(  # Компонент списка
            rx.foreach(TestsState.tests, lambda test:  # Итерация по списку тестов
                rx.list_item(  # Компонент элемента списка
                    rx.button(test.title, on_click=TestsState.select_test(test))  # Кнопка для выбора теста
                )
            )
        )
    )


# Функция для создания компонента деталей теста
def test_details():
    return rx.cond(  # Условный рендеринг
        TestsState.selected_test,  # Условие: есть выбранный тест
        rx.vstack(  # Вертикальное расположение компонентов
            rx.heading(f"Детали теста: {TestsState.selected_test.title}"),  # Заголовок деталей теста
            subject_text(),  # Предмет теста
            topic_text(),
            rx.button("Сбросить выбор", on_click=TestsState.clear_selected_test),  # Кнопка для сброса выбора теста
            test_text_all(),  # Вызов функции для генерации представления теста
            # rx.button("Проверить ответы", on_click=TestsState.),
              # Кнопка для обновления списка тестов

        ),
        rx.text("Выберите тест из списка"),  # Текст, если тест не выбран
    )


# Функция для создания компонента формы добавления теста
def add_test_form():
    return rx.vstack(  # Вертикальное расположение компонентов
        rx.heading("Добавить тест"),  # Заголовок формы добавления теста
        rx.input(  # Поле ввода для названия теста
            placeholder="Название теста",  # Подсказка
            on_change=TestsState.handle_title_change,  # Обработчик изменения
            value=TestsState.new_test_title,  # Значение поля ввода
        ),
        rx.input(  # Поле ввода для предмета теста
            placeholder="Предмет теста",  # Подсказка
            on_change=TestsState.handle_subject_change,  # Обработчик изменения
            value=TestsState.new_test_subject,  # Значение поля ввода
        ),
        rx.input(  # Поле ввода для предмета теста
            placeholder="Тема теста",  # Подсказка
            on_change=TestsState.handle_topic_change,  # Обработчик изменения
            value=TestsState.new_test_topic,  # Значение поля ввода
        ),
        rx.text_area(  # Многострочное поле ввода для JSON данных теста
            placeholder="Тест",  # Подсказка
            on_change=TestsState.handle_text_change,  # Обработчик изменения
            value=TestsState.new_test_text,  # Значение поля ввода
        ),
        rx.cond(TestsState.error_message, rx.text(TestsState.error_message, color="red")),
        # Вывод сообщения об ошибке, если оно есть
        rx.button("Добавить тест", on_click=TestsState.add_test),  # Кнопка для добавления теста
    )


# Функция для создания главной страницы приложения
def index():
    return rx.hstack(  # Горизонтальное расположение компонентов
        rx.vstack(test_list(), add_test_form()),  # Вертикальное расположение списка тестов и формы добавления
        test_details(),  # Компонент деталей теста
        spacing="2",  # Расстояние между компонентами
    )
