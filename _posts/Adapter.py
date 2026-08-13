from abc import ABC, abstractmethod
import json


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,payment_data):
        pass 

class LegacyPaymentSystem:
    def setup_payment(self,amount_in_GBP):                  #Old SOAP-based API
        print(f"Legacy system processed payment of {amount_in_GBP}")

# create the Adapter 

class paymentAdapter(PaymentProcessor):  

    def __init__(self,legacy_system):
        self.legacy_system =legacy_system

    def pay(self,payment_data):

        payment=json.loads(payment_data)
        self.legacy_system.setup_payment(payment["amount"])



class EcommercePlatform:                               #Modern E-commerce platform
                                                              # expecting RESTful JSON APIs
    def __init__ (self,Payment_Processor):    
        self.payment_processor=Payment_Processor

    def  checkout(self,amount):

        print("processing payment!!!")  
        payment_data=json.dumps({
            "amount":amount,
            "currency":"GBP"
        })

        self.payment_processor.pay(payment_data)

if __name__ == "__main__":
      
      legacy_payment=LegacyPaymentSystem()

      payment_adapter= paymentAdapter(legacy_payment)  

      Ecommerce = EcommercePlatform(payment_adapter)   #connect the Adapter to the Modern e_commerce platform

      Ecommerce.checkout(50)

