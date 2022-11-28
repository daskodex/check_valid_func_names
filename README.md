В этом репозитории находится решение тестовой задачи для Яндекс.Практикум.

Пояснение:
main.py - основной файл проекта
students_works - директория с работами студентов
tests.py - файл с тестами

Задание:
По нашему Правилу обучающиеся в присылаемых решениях должны имена всех
функций/методов, определенных внутри класса, начинать только с маленькой
латинской буквы, а имена функций, определенных вне класса, начинать только с
большой латинской буквы. Решение студента поступает к нам в виде .py файла.
При этом мы не знаем, будет ли код, написанный студентом, синтаксически
корректным. Разработайте скрипт проверки Правила, которому на вход будет
подаваться файл со студенческим кодом; при корректном коде и выполнении
Правила выходное значение скрипта должно быть равно 0, во всех остальных
случаях 1.

Примеры:
#Пример кода где Правило выполняется
def CircleFactory():
print('hello')
print('world')

class Triangle():
def method_one(self):
pass
def method_two(self):
pass

#Пример кода, где Правило не выполняется
def triangleFactory():
print('hello')
print('world')

Тестовое задание 2
class Round():
def _method_one(self):
pass
def method_two(self):
pass