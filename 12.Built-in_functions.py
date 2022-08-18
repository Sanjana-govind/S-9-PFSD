#Built-in attributes
class student:
    def __init__(self,id,name,email,cgpa):
        self.id=id
        self.name=name
        self.email=email
        self.cgpa=cgpa
ob=student(1234,"sanjana","xyz.gmail.com",9.1)
print(getattr(ob,"name"))                        #get attribute

setattr(ob,'id',4321)                            #set attribute
print(getattr(ob,"id"))       #1234 is changed to 4321

print(getattr(ob,"email"))
delattr(ob,'email')                             #del attribute
#print(getattr(ob,"email"))

print(hasattr(ob,"name"))                       #has attribute
print(hasattr(ob,"email"))