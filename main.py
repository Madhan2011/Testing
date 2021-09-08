class Test:

    def __init__(self):
        self.a = int(input("a : "))
        self.b = int(input("b : "))

    def addition(self):
        print(self.a + self.b)

    def subtraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)


if __name__ == '__main__':
    obj = Test()
    obj.addition()
    obj.subtraction()
    obj.multiplication()
    obj.division()








