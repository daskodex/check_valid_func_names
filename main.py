"""
Для реализации решения используйте python 3.8

Формализованное задание:

1.Имена всех функций/методов, определенных внутри класса
+ начинать только с маленькой буквы
+ с латинской буквы

2.Имена функций, определенных вне класса:
+ начинать только большой буквы
+ начинить только с латинской буквы

3.При этом мы не знаем, будет ли код, написанный студентом, синтаксически
корректным

Новые вводные:

- учитывал возможную вложенность [x]
- учитывал возможно некорректный синтаксис [x]
- и просьба обратить внимание на возможности стандартной библиотеки [x]

Комментарии от сотрудников Яндекса:

>Включил в код прям перечень Больших и маленьких букв. Для кейсов со
 вложенностью классов не будет работать [x]

>Исполняет код студента - не сработает при синтаксической или динамической ошибке [x]

"""

import ast
import re


def check_valid_functions_names(user_file_name: str, print_log: int = 0) -> int:
    """ new function for class and function validation """

    check_error = 0
    errors_log = [user_file_name]

    upper_case_chars = re.compile("[A-Z]")
    lower_case_chars = re.compile("[a-z]")

    try:
        with open(user_file_name, "r", encoding="utf-8") as source:
            node = ast.parse(source.read(), mode='exec')
    except SyntaxError:
        return 1

    objects_id_type = {}

    """ формируем словарь objects_id_type: id ребенка <-> тип родителя """
    for parent_node in ast.walk(node):
        for child_node in ast.iter_child_nodes(parent_node):
            parent_type = ''

            if isinstance(parent_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                parent_type = 'function'

            if isinstance(parent_node, ast.ClassDef):
                parent_type = 'class'

            """ создаем словарь id объекта : тип родителя ('',class,function)"""
            objects_id_type[id(child_node)] = parent_type

    """ перебираем все функции и классы произвольной степени вложенности """
    for sub_node in ast.walk(node):

        """ ищем функции\методы """
        if isinstance(sub_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            parent_type = ''
            if id(sub_node) in objects_id_type:
                parent_type = objects_id_type[id(sub_node)]

            if parent_type == '' or parent_type == 'function':
                if not upper_case_chars.match(sub_node.name[0]):
                    errors_log.append(f'{sub_node.lineno} Bad function name {sub_node.name} wrong char "{sub_node.name[0]}" ')
                    check_error = 1

        """ ищем классы """
        if isinstance(sub_node, ast.FunctionDef):
            parent_type = ''
            if id(sub_node) in objects_id_type:
                parent_type = objects_id_type[id(sub_node)]

            if parent_type == 'class':
                if not lower_case_chars.match(sub_node.name[0]):
                    errors_log.append(f'{sub_node.lineno} Bad function {sub_node.name} INSIDE CLASS wrong char "{sub_node.name[0]}" ')
                    check_error = 1

    if print_log == 1:
        print(ast.dump(node, indent=4, annotate_fields=False))
        print('\n'.join(errors_log))

    return check_error


if __name__ == "__main__":
    file_name = 'c:\\source\\python\\check_valid_func_names\\students_works\\test_student_work_0.py'

    result = check_valid_functions_names(file_name,1)

    print(f'Check errors: {result}')
