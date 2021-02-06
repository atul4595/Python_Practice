class Employee:
    no_of_leaves=8
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printdetails(self):
        return f"The name is {self.name}. age is {self.age} and gender is {self.gender}"

    @classmethod
    def chang_l(cls,leave):
        cls.no_of_leaves=leave

    @classmethod
    def split(cls,string):
        return cls(*string.split("-"))

        # param=string.split("-")
        # return cls(param[0],param[1],param[2])

karan=Employee.split("Atul-31-Male")
print(karan.printdetails())




harry=Employee("Atul",31,"Male")
print(harry.printdetails())
harry.chang_l(78)