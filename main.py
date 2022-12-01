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
- учитывал возможно некорректный синтаксис
- и просьба обратить внимание на возможности стандартной библиотеки [x]

"""

import ast

# def show_info(functionNode):
#     print("Function name:", functionNode.name)
#     print("Args List:")
#     for arg in functionNode.args.args:
#         #import pdb; pdb.set_trace()
#         print("\tParameter name:", arg.arg)

def check_valid_functions_names(user_file_name: str) -> int:
    """new function for class and function validation"""
    check_error = 0
    errors_log = []

    with open(user_file_name, "r", encoding="utf-8") as source:
        node = ast.parse(source.read(), mode='exec')

    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

    for function in functions:
        if not str.isupper(function.name[0]):
            errors_log.append(f'Bad function name (outside class): { function.name } wrong char "{ function.name[0] }" ')
            check_error = 1


    for class_ in classes:
         methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
         for method in methods:
             errors_log.append(f'Bad function name (inside class): {method.name} wrong char "{method.name[0]}" ')
             check_error = 1


    #print(ast.dump(node, indent=4,annotate_fields=False))
    print('\n'.join(errors_log))

    return check_error

if __name__ == "__main__":
    file_name = 'c:\\source\\python\\check_valid_func_names\\students_works\\test_student_work_0.py'
    result = check_valid_functions_names(file_name)
    print(f'Check errors: {result}')
