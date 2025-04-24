import re
import io
import sys
import reflex as rx


class RussianPythonTranslator(rx.State):

    TRANSLATION_DICT = {
        'если': 'if',
        'иначе': 'else',
        'иначе_если': 'elif',
        'пока': 'while',
        'для': 'for',
        'в': 'in',
        'диапазон': 'range',
        'импорт': 'import',
        'из': 'from',
        'как': 'as',
        'определить': 'def',
        'класс': 'class',
        'вернуть': 'return',
        'попробовать': 'try',
        'кроме': 'except',
        'всегда': 'finally',
        'поднять': 'raise',
        'и': 'and',
        'или': 'or',
        'не': 'not',
        'истина': 'True',
        'ложь': 'False',
        'нет': 'None',
        'печать': 'print',
        'ввод': 'input',
        'длина': 'len',
        'тип': 'type',
        'список': 'list',
        'словарь': 'dict',
        'множество': 'set',
        'кортеж': 'tuple',
        'строка': 'str',
        'целое': 'int',
        'вещественное': 'float',
        'булево': 'bool',
        'открыть': 'open',
        'с': 'with',
        'утвердить': 'assert',
        'прорвать': 'break',
        'продолжить': 'continue',
        'удалить': 'del',
        'глобальное': 'global',
        'нелокальное': 'nonlocal',
        'пропустить': 'pass',
        'выдать': 'yield',
        'лямбда': 'lambda'
    }

    russian_code: str = """печать("Привет мир!")"""

    active_tab: str = "source"
    translated_code: str = ""
    execution_output: str = ""

    def translate_code(self):
        """Переводит русский код в Python с сохранением форматирования."""
        lines = self.russian_code.split('\n')
        translated_lines = []

        for line in lines:
            # Сохраняем исходные отступы в начале строки
            indent = re.match(r'^\s*', line).group()

            if '#' in line:
                line = line[:line.index('#')]

            # Разбиваем строку, сохраняя разделители
            parts = re.split(r'([а-яА-Я_][а-яА-Я0-9_]*|\W)', line)

            translated_parts = []
            for part in parts:
                if not part.strip():
                    translated_parts.append(part)
                    continue

                lower_part = part.lower()
                if lower_part in self.TRANSLATION_DICT and part.islower():
                    translated_parts.append(self.TRANSLATION_DICT[lower_part])
                else:
                    translated_parts.append(part)

            translated_line = indent + ''.join(translated_parts)
            translated_lines.append(translated_line)

        self.translated_code = '\n'.join(translated_lines)

    def execute_code(self):
        """Выполняет код и переключает на вкладку с результатом."""
        self.translate_code()
        try:
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            exec(self.translated_code, {})
            # Получаем вывод и заменяем переносы на HTML-совместимые
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            self.execution_output = output
            self.active_tab = "result"
        except Exception as e:
            self.execution_output = f"Ошибка выполнения:\n{str(e)}"
            self.active_tab = "result"
