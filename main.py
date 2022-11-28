"""
Для реализации решения используйте python 3.8

По нашему Правилу обучающиеся в присылаемых решениях должны имена всех
функций/методов, определенных внутри класса, начинать только с маленькой
латинской буквы, а имена функций, определенных вне класса, начинать только с
большой латинской буквы. Решение студента поступает к нам в виде .py файла.

При этом мы не знаем, будет ли код, написанный студентом, синтаксически
корректным. Разработайте скрипт проверки Правила, которому на вход будет
подаваться файл со студенческим кодом; при корректном коде и выполнении
Правила выходное значение скрипта должно быть равно 0, во всех остальных
случаях 1.


Правила валидации:
1.Имена всех функций/методов, определенных внутри класса, начинать только с маленькой
латинской буквы

2.Имена функций, определенных вне класса, начинать только большой латинской буквы
"""

# import test_student_work
import inspect
import importlib.util
import sys


def check_valid_func_names(user_file_name: str) -> int:
    """Функция проверяет соответствие названий функций, классов и функицй классов"""

    spec = importlib.util.spec_from_file_location("student_test_work", user_file_name)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["student_test_work"] = foo
    spec.loader.exec_module(foo)

    check_error = 0

    lower_case_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_case_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    errors_list = []

    """ Проверяем в каком регистре находится первая буква названия функции\метода внутри класса """
    for class_name, class_data in inspect.getmembers(foo, inspect.isclass):
        for class_function_name, class_function_data in inspect.getmembers(class_data, inspect.isfunction):
            if not class_function_name.startswith('__'):
                if not class_function_name[0] in lower_case_chars:
                    check_error = 1
                    errors_list.append(class_function_name)

    """ Проверяем в каком регистре находится первая буква имени функции вне классов """
    for function_name, function_data in inspect.getmembers(foo, inspect.isfunction):
        if not function_name.startswith('__'):
            if not function_name[0] in upper_case_chars:
                check_error = 1
                errors_list.append(function_name)

    #print(errors_list)

    return check_error


if __name__ == "__main__":
    file_name = 'students_works/test_student_work_ok.py'
    result = check_valid_func_names(file_name)
    print(f'Check errors: {result}')
