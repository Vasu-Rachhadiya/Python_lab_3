class Calculator:
    def __init__(self):
        self.__result = 0
    def add(self, a, b):
        self.__result = a + b
    def subtract(self, a, b):
        self.__result = a - b
    def get_result(self):
        return self.__result
calc = Calculator()
calc.add(10, 5)
print("Addition    : ", calc.get_result())
calc.subtract(10, 5)
print("Subtraction : ", calc.get_result())