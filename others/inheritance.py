class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old!")
    
    def speak(self):
        print("I dont know how to speak")
       
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # call the motherclass init
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")
    

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()

c = Cat('Bill', 34, 'caramel')
c.speak()
c.show()

d = Dog('Gill', 29)
d.speak()

f = Fish("Bubles", 2)
f.speak()
