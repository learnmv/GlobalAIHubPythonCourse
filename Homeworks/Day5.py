#Question

#Create three classes named Animals, Dogs and Cats. Add some
# features to these classes. Create some functions with these attributes.
# Don't forget! You have to do it using inheritance.


class Animals():
    def __init__(self,name,tail,four_legs):
        self.name = name
        self.tail = tail
        self.four_legs = four_legs

class Dog(Animals):
    def __init__(self,name,tail,four_legs):
        super().__init__(name,tail,four_legs)
    
    def sound(self):
        print("Dog sounds like Bow...Bow....")

class Cats(Animals):
    def __init__(self,name,tail,four_legs):
        super().__init__(name,tail,four_legs)
    
    def sound(self):
        print("Cat Sounds like Meow...Meow")

dog = Dog("snoopy",True,True)
dog.sound()

cat = Cats("sweety",True,True)
cat.sound()