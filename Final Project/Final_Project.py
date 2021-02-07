#Company Management System
#Determine the names and ages of the employees
# company managers and the langauages they can speak
# Then write a program that will print the languages that
# any of the employees can speak
# In this project complete the project by creating two classes
# Employees and Manager.

class Employees():
    def __init__(self,name,age,languages):
        self.name = name
        self.age = age
        self.languages = languages
    
    def languages_speak(self):
        print(f"Languages spoken by {self.name} are :")
        for language in self.languages:
            print(language)
    
    def get_deatails(self):
        print(f"name of Employee is {self.name} and age of employee is {self.age}")

class Manager(Employees):
    def __init__(self,name,age,is_manager,languages):
        super().__init__(name,age,languages)
        self.is_manager = is_manager

    def experience(self):
        print("Experience of manager is above 10 years")
    
    def get_deatails(self):
        print(f"Name of Manager is {self.name} and age is {self.age}")

E1 = Employees(name="Arun",age=22,languages=["Hindi","English","Telugu"])
M1 = Manager(name="Avinash",age=40,is_manager=True,languages=['Hindi','Tamil','English'])
E1.languages_speak()
M1.languages_speak()
M1.experience()
E1.get_deatails()
M1.get_deatails()
