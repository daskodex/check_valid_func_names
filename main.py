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

Новые вводные:

- учитывал возможную вложенность
- учитывал возможно некорректный синтаксис [x]
- и просьба обратить внимание на возможности стандартной библиотеки [x]

Комментарии от сотрудников Яндекса:

>Включил в код прям перечень Больших и маленьких букв. Для кейсов со
 вложенностью классов не будет работать.

>Исполняет код студента - не сработает при синтаксической или динамической ошибке

"""

import ast

lower_case_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def check_valid_functions_names(user_file_name: str) -> int:
    """new function for class and function validation"""
    check_error = 0
    errors_log = []
    functions_id = []

    try:
        with open(user_file_name, "r", encoding="utf-8") as source:
            node = ast.parse(source.read(), mode='exec')
    except SyntaxError:
        return 1

    """ ищем функции вне классов """
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if not function.name[0] in upper_case_chars:
            errors_log.append(f'Bad function name (outside class): {function.name} wrong char "{function.name[0]}" ')
            check_error = 1
        functions_id.append(id(function))

    """ ищем все функции произвольной вложенности """
    all_functions = [node
        for node in ast.walk(node)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    for func in all_functions:
        if not id(func) in functions_id:
            if not func.name[0] in lower_case_chars:
                errors_log.append(f'Bad function name (inside class): {func.name} wrong char "{func.name[0]}" ')
                check_error = 1

    # print(ast.dump(node, indent=4,annotate_fields=False))
    print('\n'.join(errors_log))

    return check_error


if __name__ == "__main__":
    file_name = 'c:\\source\\python\\check_valid_func_names\\students_works\\test_student_work_0.py'
    result = check_valid_functions_names(file_name)
    print(f'Check errors: {result}')
