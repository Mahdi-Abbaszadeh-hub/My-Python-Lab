# Easy practice just instantiate
class Employee:
    def __init__(self, name, family, salary="3000$"):
        self.name = name
        self.family = family
        self.salary = salary

    def print_info(self):
        return f"hi i'm {self.name} and my last name is {self.family}\nI give {self.salary} salary"


Obj_1 = Employee("ali", "fariba")
Obj_2 = Employee("reza", "akbari", "5000$")
print(Obj_1.print_info())
print(Obj_2.print_info())

# ---------------------------------
