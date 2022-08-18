class Parent:
    def fn1(self):
        print("This is parent class")
    def fn2(self):
        print("Good morning")


class Child(Parent):
    def fn1(self):
        print("This is Child class")

ob=Child()
ob.fn1()
ob.fn2()