from abc import ABC, abstractmethod

#Abstract base class defining the common interface for electronic devices 

class ElectronicDevice (ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Implementation 
class TV(ElectronicDevice):
    

    def turn_on (self):
        print("TV is  now ON")


    def  turn_off(self):
        print("TV is now OFF") 


class Radio(ElectronicDevice):
   
    def  turn_on(self):
        print("Radio is now ON")  

    def turn_off(self):
       print("Radio is now OFF")

#Remot control that can work with any ElectronicDevice

class RemoteControl:                   
    def __init__ (self,device:ElectronicDevice ):   
       self.device =device   

    def turn_on(self):
        self.device.turn_on()

    def  turn_off(self):
        self.device.turn_off() 


class AdvancedRemoteControl(RemoteControl):    # Ability to add extra function
      
      def stop_timer(self,hours):
         print(f"Dvice will turn off within {hours}hours")


if __name__=="__main__":
             
     tv = TV()
     basic_remote = RemoteControl(tv)

     basic_remote.turn_on()
     basic_remote.turn_off()

     print()

    
     radio=Radio()
     basic_radio_remote = RemoteControl(radio)
     basic_radio_remote.turn_on()
     basic_radio_remote.turn_off()

     print()


     advanced_romte=AdvancedRemoteControl(tv)
     advanced_romte.turn_on()
     advanced_romte.stop_timer(3)
     advanced_romte.turn_off()


         







