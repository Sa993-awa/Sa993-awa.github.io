
class Vehicle:                                               # Constructor method to initialize attributes
    def __init__(self,brand,fuel_type):    
        self.brand = brand                                   # Attribute
        self.fuel_type = fuel_type                           # Attribute
                       
class Car(Vehicle):                                          # Create a subclass Car 

    def __init__(self,brand,fuel_type,num_doors):            # adds num_doors as an additional attribute
        super().__init__(brand,fuel_type)
        self.num_doors=num_doors

my_car = Car("Mercedes","petrol",4)           # Creating objects from the Car class

print("brand:",my_car.brand)
print("fuel type:",my_car.fuel_type)
print("num_doors:",my_car.num_doors)
