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
def TriangleFactory():
    print('hello')
    print('world')


class Round():
    def method_one(self):
        pass
    def method_two(self):
        pass

    class SomeInnerClass:
        def _inclass_method_one(self):
            pass

        def _incalss_method_two(self):
            pass

        def _incalss_method_three(self):
            pass