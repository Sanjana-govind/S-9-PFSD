#Constructors
#parameterized constructor
class Student:
	def __init__(self,id,name):
		self.id=id
		self.name=name

	def display(self):
		print(self.id,self.name)

std1=Student(10,"ABC")
std2=Student(20,"DEF")
std1.display()
std2.display()


#Non_Parameterized constuctor

class Student1:
    count=0
    def __init__(self):
        Student1.count=Student1.count+1
s1=Student1()
s2=Student1()
s3=Student1()
print("Total Count:",Student1.count)

#More than one constructor in a single class

class Student3:
    def __init__(self):
        print("This is my first constructor")
    def __init__(self):
        print("This is my second constructor")
std = Student3()                         #output will be the latest constructor declared in the class.