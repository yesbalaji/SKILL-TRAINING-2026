class Demo:
    a = 10
    b = 20

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def display(self):
        print(self.c, self.d)

    def c1(self, new):
        self.c = new

    @classmethod
    def show(cls):
        print(cls.a, cls.b)

    @staticmethod
    def msg():
        print("Public Access Specifiers")


user = Demo(10, 20)

user.display()
user.c1(40)
user.display()
Demo.show()
Demo.msg()