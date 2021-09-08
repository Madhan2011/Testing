class Test:

    def __init__(self):
        self.a = int(input("a : "))
        self.b = int(input("b : "))

    def name(self):
        print(self.a + self.b)


if __name__ == '__main__':
    obj = Test()
    obj.name()
