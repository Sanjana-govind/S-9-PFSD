#function arguments
#1.Default arguments
def sample(num1,num2=10):
    print(num1)
    print(num2)


sample(5, 20)

#2.Keyword arguments
def sample1(num3=20, num4=30):
    print(num3)
    print(num4)

sample1(5, 10)
sample1(num3=40, num4=10)

#3.Required arguments.
def sample2(num5=20, num6=30):
    print(num5)
    print(num6)

sample2(5, 10)
sample2(10)