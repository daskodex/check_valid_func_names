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
import pylint.lint
from pylint.lint import Run
from pylint.reporters.text import TextReporter


class WritableObject(object):
    """dummy output stream for pylint"""
    def __init__(self):
        self.content = []
    def write(self, st):
        self.content.append(st)
    def read(self):
        return self.content

#C0103: Function name "TriangleFactory" doesn't conform to snake_case

def check_valid_functions_names(user_file_name: str) -> int:
    """new function for class and fucntion validation"""
    check_error = 0
    pylint_errors = []
    pylint_output = WritableObject()

    """
    C0103: Function name "triangleFactory" doesn't conform to PascalCase naming style (invalid-name)
    """
    pylint_erros_code_list = ['C0103']

    ARGS = ["-r","n","--rcfile=./.pylintrc"]

    Run([user_file_name]+ARGS, reporter=TextReporter(pylint_output), exit=False)

    for output_line in pylint_output.read():
        print(output_line)

        pylint_errors.append(output_line)

    return check_error


if __name__ == "__main__":
    file_name = 'c:\\source\\python\\check_valid_func_names\\students_works\\test_student_work_0.py'
    result = check_valid_functions_names(file_name)
    print(f'Check errors: {result}')
