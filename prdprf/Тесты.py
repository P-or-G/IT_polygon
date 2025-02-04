import reflex as rx
import json
from typing import Dict, Any

# Константы
INVALID_JSON_ERROR = "Некорректный JSON формат"
TEST_NOT_SELECTED = "Тест не выбран"
LOAD_TEST_ERROR = "Ошибка загрузки данных теста"
NO_TESTS_IN_DATABASE = "База данных пуста, добавлены примеры"

# Модель данных для хранения тестов в базе данных
class Test(rx.Model, table=True):
    title: str | None = None # Название теста
    subject: str | None = None # Предмет теста
    json_data_as_string: str = ""  # JSON данные теста в виде строки

    @property  # Декоратор для создания свойства, позволяющего работать с JSON как со словарем
    def json_data(self) -> Dict[str, Any]:
        """Получить JSON данные в виде словаря."""
        try:
            return json.loads(self.json_data_as_string)  # Преобразование JSON строки в словарь Python
        except (json.JSONDecodeError, TypeError):  # Обработка ошибок преобразования JSON
            return {}  # Возврат пустого словаря, если произошла ошибка

    @json_data.setter  # Декоратор для установки JSON данных из словаря
    def json_data(self, value: Dict[str, Any]):
        """Установить JSON данные из словаря, сохранив строку."""
        try:
            self.json_data_as_string = json.dumps(value)  # Преобразование словаря Python в JSON строку
        except TypeError:
            self.json_data_as_string = ""  # Установка пустой строки, если преобразование не удалось

    def update_json_data(self, key: str, value: Any):
        """Обновить или добавить поле в json"""
        data = self.json_data  # Получение текущих JSON данных
        data[key] = value  # Обновление или добавление значения по ключу
        self.json_data = data  # Установка обновленных JSON данных


# Класс State для управления состоянием приложения
class State(rx.State):
    tests: list[Test] = []  # Список тестов, загруженных из базы данных
    selected_test: Test = None  # Выбранный тест для просмотра деталей
    new_test_title: str = ""  # Название нового теста
    new_test_subject: str = ""  # Предмет нового теста
    new_test_json_data_as_string: str = ""  # JSON данные нового теста в виде строки
    error_message: str = ""  # Сообщение об ошибке

    def on_mount(self):
        """Вызывается при монтировании страницы, загружает данные и если их нет, то добавляет тестовые данные"""
        self.fetch_tests()  # Загрузка тестов из базы данных
        with rx.session() as session:  # Создание сессии для работы с базой данных
            if not session.query(Test).first():  # Проверка, есть ли тесты в базе данных
                self.load_and_add_json()  # Загрузка и добавление тестовых данных
            else:
                self.error_message = NO_TESTS_IN_DATABASE # Показать сообщение, что добавлены примеры

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

    def handle_json_data_change(self, json_data):
        """Обработчик изменения JSON данных нового теста"""
        self.new_test_json_data_as_string = json_data  # Обновление JSON данных нового теста

    def add_test(self):
        """Добавление нового теста в базу данных"""
        try:
            json_data = json.loads(self.new_test_json_data_as_string)  # Преобразование JSON строки в словарь Python
        except json.JSONDecodeError:  # Обработка ошибки преобразования JSON
            self.error_message = INVALID_JSON_ERROR  # Установка сообщения об ошибке
            return  # Выход из функции, если JSON некорректный

        with rx.session() as session:  # Создание сессии для работы с базой данных
            new_test = Test(title=self.new_test_title, subject=self.new_test_subject)  # Создание объекта Test
            new_test.json_data = json_data  # Установка JSON данных теста
            session.add(new_test)  # Добавление теста в базу данных
            session.commit()  # Сохранение изменений

        self.error_message = ""  # Сброс сообщения об ошибке
        self.new_test_title = ""  # Сброс названия нового теста
        self.new_test_subject = ""  # Сброс предмета нового теста
        self.new_test_json_data_as_string = ""  # Сброс JSON данных нового теста
        self.fetch_tests()  # Обновление списка тестов


    def _format_tasks(self, tasks) -> list:
        """Форматирование списка заданий в текстовом виде."""
        task_lines = []

        for index, task in enumerate(tasks):
            question = task.get('question', 'вопрос отсутствует')
            points = task.get('points', 0)
            answers = task.get('answers', [])
            answers_text = f" Ответы: {', '.join(answers)}" if answers else ""

            task_line = f"{index + 1}. {question} (Баллы: {points}){answers_text}"
            task_lines.append(task_line)

        return task_lines
    def generate_test(self) -> str:
        """Генерация представления выбранного теста."""

        # Проверка, выбран ли тест
        if not self.selected_test:
            return TEST_NOT_SELECTED  # Возврат текста, если тест не выбран

        # Проверка наличия json_data
        if not hasattr(self.selected_test, 'json_data'):
            error_message = "Ошибка: Данные теста отсутствуют."
            print(error_message)
            return error_message

        # Получение JSON данных теста
        test_data = self.selected_test.json_data
        test_text = f"Предмет: {self.selected_test.subject}\n"

        # Добавление темы
        theme = test_data.get('theme', 'неизвестно')
        test_text += f"Тема: {theme}\n\nЗадания:\n"

        # Получение списка заданий
        tasks = test_data.get("tasks", [])

        if tasks:
            task_lines = self._format_tasks(tasks)  # Формирование текста для заданий
            test_text += "\n".join(task_lines)
        else:
            test_text += "Задания отсутствуют"

        return rx.text(test_text)  # Возврат компонента rx.text с сгенерированным текстом



    def load_json_data(self, file_path):
        """Загрузка JSON данных из файла"""
        with open(file_path, "r") as file:  # Открытие файла
            return json.load(file)  # Загрузка JSON данных

    def load_and_add_json(self):
        """Загрузка и добавление тестовых данных из файла test_data.json"""
        try:
            json_data = self.load_json_data("test_data.json")  # Загрузка JSON данных из файла
            new_test = Test(title="Пример теста", subject="Математика")  # Создание объекта Test
            new_test.json_data = json_data  # Установка JSON данных теста
            with rx.session() as session:  # Создание сессии для работы с базой данных
                session.add(new_test)  # Добавление теста в базу данных
                session.commit()  # Сохранение изменений
        except Exception as e:  # Обработка ошибок
            self.error_message = f"{LOAD_TEST_ERROR}: {e}" # Сообщение об ошибке
            print(f"Ошибка: {e}") # Вывод ошибки в консоль

def subject_text():
    """Возвращает текст с предметом текущего теста"""
    return rx.text(f"Предмет: {State.selected_test.subject}")

# Функция для создания компонента списка тестов
def test_list():
    return rx.vstack(  # Вертикальное расположение компонентов
        rx.heading("Список тестов"),  # Заголовок списка тестов
        rx.button("Обновить", on_click=State.fetch_tests),  # Кнопка для обновления списка тестов
        rx.list(  # Компонент списка
           rx.foreach(State.tests, lambda test:  # Итерация по списку тестов
                rx.list_item(  # Компонент элемента списка
                  rx.button(test.title, on_click=State.select_test(test)) # Кнопка для выбора теста
                )
            )
        )
    )

# Функция для создания компонента деталей теста
def test_details():
    return rx.cond(  # Условный рендеринг
        State.selected_test,  # Условие: есть выбранный тест
        rx.vstack(  # Вертикальное расположение компонентов
            rx.heading(f"Детали теста: {State.selected_test.title}"),  # Заголовок деталей теста
            subject_text(), # Предмет теста
            rx.button("Сбросить выбор", on_click=State.clear_selected_test),  # Кнопка для сброса выбора теста
            rx.text(State.generate_test()),  # Вызов функции для генерации представления теста
        ),
        rx.text("Выберите тест из списка"),  # Текст, если тест не выбран
    )

# Функция для создания компонента формы добавления теста
def add_test_form():
    return rx.vstack(  # Вертикальное расположение компонентов
        rx.heading("Добавить тест"),  # Заголовок формы добавления теста
        rx.input(  # Поле ввода для названия теста
            placeholder="Название теста",  # Подсказка
            on_change=State.handle_title_change,  # Обработчик изменения
            value=State.new_test_title,  # Значение поля ввода
        ),
        rx.input(  # Поле ввода для предмета теста
            placeholder="Предмет теста",  # Подсказка
            on_change=State.handle_subject_change,  # Обработчик изменения
            value=State.new_test_subject,  # Значение поля ввода
        ),
        rx.text_area(  # Многострочное поле ввода для JSON данных теста
            placeholder="JSON данные теста",  # Подсказка
            on_change=State.handle_json_data_change,  # Обработчик изменения
            value=State.new_test_json_data_as_string,  # Значение поля ввода
        ),
        rx.cond(State.error_message, rx.text(State.error_message, color="red")),  # Вывод сообщения об ошибке, если оно есть
        rx.button("Добавить тест", on_click=State.add_test),  # Кнопка для добавления теста
    )

# Функция для создания главной страницы приложения
def index():
    return rx.hstack(  # Горизонтальное расположение компонентов
        rx.vstack(test_list(), add_test_form()),  # Вертикальное расположение списка тестов и формы добавления
        test_details(),  # Компонент деталей теста
        spacing="2",  # Расстояние между компонентами
    )

app = rx.App()  # Создание экземпляра приложения Reflex
app.add_page(index)  # Добавление страницы в приложение
