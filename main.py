"""
Для реализации решения используйте python 3.8

Правила валидации:
1.Имена всех функций/методов, определенных внутри класса, начинать только с маленькой
латинской буквы

2.Имена функций, определенных вне класса, начинать только большой латинской буквы

3.При этом мы не знаем, будет ли код, написанный студентом, синтаксически
корректным

Новые вводные:

- учитывал возможную вложенность [x]
- учитывал возможно некорректный синтаксис [x]
- и просьба обратить внимание на возможности стандартной библиотеки [x]

Комментарии от сотрудников Яндекса:

>Включил в код прям перечень Больших и маленьких букв. Для кейсов со
 вложенностью классов не будет работать.

>Исполняет код студента - не сработает при синтаксической или динамической ошибке

"""

import ast, re

def check_valid_functions_names(user_file_name: str) -> int:
    """new function for class and function validation"""
    check_error = 0
    errors_log = []
    first_level_functions_id = []

    upper_case_chars = re.compile("[A-Z]")
    lower_case_chars = re.compile("[a-z]")

    try:
        with open(user_file_name, "r", encoding="utf-8") as source:
            node = ast.parse(source.read(), mode='exec')
    except SyntaxError:
        return 1

    """ ищем функции вне классов без вложенности """
    for function in node.body:
        if isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not upper_case_chars.match(function.name[0]):
                errors_log.append(f'Bad function name (outside class): {function.name} wrong char "{function.name[0]}" ')
                check_error = 1
            first_level_functions_id.append(id(function))

    """ ищем все функции произвольной вложенности """
    for sub_node in ast.walk(node):
        if isinstance(sub_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not id(sub_node) in first_level_functions_id:
                if not lower_case_chars.match(sub_node.name[0]):
                    errors_log.append(f'Bad function name (inside class): {sub_node.name} wrong char "{sub_node.name[0]}" ')
                    check_error = 1

    for snode in ast.walk(node):
        for child in ast.iter_child_nodes(snode):
            child.parent = snode

    # print(ast.dump(node, indent=4,annotate_fields=False))
    print('\n'.join(errors_log))

    return check_error


if __name__ == "__main__":
    file_name = 'c:\\source\\python\\check_valid_func_names\\students_works\\test_student_work_0.py'
    result = check_valid_functions_names(file_name)
    print(f'Check errors: {result}')
