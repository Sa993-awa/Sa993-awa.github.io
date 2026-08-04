from abc import ABC, abstractmethod

class Animal(ABC):                      # Abstract class
    @abstractmethod
    def make_sound(self):
        pass

class Dog (Animal):                     # Implement subclasses Dog

    def make_sound(self):
        return"woooof"

class Cat (Animal):                     # Implement subclasses Cat
    def make_sound(self): 
        return"Meooow"   


dog = Dog()                            # Creating objects
cat = Cat()                            # Creating objects             
    
print(dog.make_sound())                # Calling methods  
print(cat.make_sound())                # Calling methods