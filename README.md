 __     __     _____           _    _   _ _                    
 \ \   / /    |  __ \         | |  | | (_) |                   
  \ \_/ /_ _  | |__) | __ __ _| | _| |_ _| | ___   _ _ __ ___  
   \   / _` | |  ___/ '__/ _` | |/ / __| | |/ / | | | '_ ` _ \ 
    | | (_| |_| |   | | | (_| |   <| |_| |   <| |_| | | | | | |
    |_|\__,_(_)_|   |_|  \__,_|_|\_\\__|_|_|\_\\__,_|_| |_| |_|

В этом репозитории находится решение тестовой задачи для Яндекс.Практикум.

Структура проекта:
main.py - основной файл проекта
students_works - директория с работами студентов
tests.py - файл с тестами (pytest)
requarements.txt - список внешних зависимостей для pip

Версии

v0.3 Переписано на встроенном модуле ast+re
v0.2 Переписано на основе модуля pylint
v0.1 Сделано на основе модуля inspect

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