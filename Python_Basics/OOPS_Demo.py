class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.SecondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.SecondNumber + Calculator.num


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData(),
print(obj.Summation())

obj = Calculator(4, 5)  # syntax to create objects in python
obj.getData(),
print(obj.Summation())
