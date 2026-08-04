class Person:                                          # Constructor method to initialize the person's name
    def __init__(self,name):
        self.name = name
        print(f"GoodMorning,{self.name}!!!")


    def __del__(self):                                  # Destructor method called when the object is deleted
        print(f"Goodbye,{self.name}!!!")


person_name = Person("Sali")                            # Creating an object of Person class
del person_name                                         # delete the object explicitly    


