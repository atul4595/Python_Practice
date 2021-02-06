class Employee:
    no_of_leaves=8
    def __init__(self,Name,age,Gender):
        self.Name=Name
        self.age=age
        self.Gender=Gender

    def print_details(self):
        return f"I am {self.Name}. My age is {self.age} and gender is{self.Gender}"

    @classmethod
    def Chnage_l(cls,leave):
        cls.no_of_leaves=leave

    @classmethod
    def Spli_P(cls,String):
        param=String.split("-")
        return cls(param[0],param[1],param[2])

    @staticmethod
    def print_s():
        return "Hello"

class Programmer(Employee):
    def __init__(self,Name,age,Gender,arole):
        self.Name=Name
        self.age=age
        self.Gender=Gender
        self.arole=arole

    def printprog(self):
        return f"The name is {self.Name}. age is {self.age} and geder is {self.Gender} and language is {self.arole}"

Harry=Employee("Harry",31,"Male")
Rohan=Employee("Rohan",31,"Male")

shubham= Programmer("Shubham","31","Male",["C#","Python"])
print(shubham.print_details())
