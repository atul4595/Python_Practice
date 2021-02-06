class Employee:
    no_of_leaves=12
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_info(self):
        return f"My name ia {self.name}. age is {self.age} and gender is {self.gender}"

    @classmethod
    def change_l(cls,leaves):
        cls.no_of_leaves=leaves

    @classmethod
    def strip(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def print_h():
        return "Hello"

class player():
        no_of_games=4
        def __init__(self,name,game):
            self.name=name
            self.game=game

        def printdetails(self):
            return f"The name is{self.name}. Game is {self.game}"

class Coolprogrammer(Employee,player):
    pass

rahul=Coolprogrammer("rahul",12,"Male")
print(rahul.print_info())

