
class BankAccount:                                     # BankAccount with a private attribute 
    def __init__(self,balance):
         self.__balance= balance


    def deposit (self,amount):
         if amount > 0: 
           self.__balance += amount
           print (f"Deposited {amount} successfully") 
         else:
             print("Invaild deposit amount")  

    def withdraw (self,amount):     
            if amount > self.__balance:
             print( "Insufficient balance")                # Check if there is enough money
        
            elif amount<=0:                                     # Withdrawal amount must be positive
             print("invalid withdraw amount")
            else:
                self.__balance-=amount
                print (f"withdraw {amount} successfully")

    def get_balance(self):
        return self.__balance   
        

if __name__ == "__main__":                                  # Display account information
    account = BankAccount(                                   
             1500
             )

print("current balance:", account.get_balance())

account.deposit(600)                                         # Apply deposit        
account.withdraw(300)                                        # Apply deposit 

print("Final balance:", account.get_balance())              # Apply the final balance
        