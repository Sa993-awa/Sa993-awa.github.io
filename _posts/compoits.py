from abc import ABC, abstractmethod
#commen interface for all school components
class SchoolComponent(ABC):
    @abstractmethod
    def show(self):
        pass


#represent an individual class
class Class(SchoolComponent):
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour


    def show(self):
        print(f"Class:{self.name} - colour:{self.colour}")


#represent a year group
class YearGroup(SchoolComponent):      #common interface

    def __init__(self,year):
        self.year=year
        self.children=[]

    def add(self,component):
        self.children.append(component)

    def show(self):
        print(f"{self.year}")

        for child in self.children:
            child.show()

class School(SchoolComponent):
    def __init__(self,name):
         self.name=name
         self.children=[]

    def add(self,component):
        self.children.append(component)  

    def show(self) :
        print(f"School:{self.name}")  

        for child in self.children:
            child.show()

#create the school
school = School("infant school")          

#create year groups

Year1=YearGroup("Year 1")
Year2=YearGroup("Year 2")

#create classes with different colours
blue_class=Class("Blue Class","Blue")
green_class=Class("Green class","Green")


red_class=Class("Red Class","Red")
orange_class=Class("Orange Class","Orange")


Year1.add(blue_class)
Year1.add( green_class)

Year2.add(red_class)
Year2.add(orange_class)


school.add(Year1)
school.add(Year2)

school.show()


