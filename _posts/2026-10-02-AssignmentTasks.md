---
layout: post
title: AssignmentTasks
subtitle: Journey into advanced OOP concepts
categories: markdown
tags: [Task1, Task2 ,Task3, Task4 ]
---   

### Task1: Summarise Key Learning Outcomes:   

#### Reflect on Learning Objectives: Provide a summary of how you have achieved the module’s learning objectives:   

     -Understand and implement secure coding practices in software development.   

     -Apply advanced object – oriented principles to solve complex software problems.   

     -Utilise design patterns to create reusable, maintainable, and flexible code.  

      -Briefly extend your reflection to include:   

        1.\ Advanced design pattterns (practical application):mention hands-on use of Strategy, Decorator, Visitor and                Abstract Factory, explicitly linking them to:   

         -Runtime behavioural flexibility.   

        -Seperation of concerns.   

        -Scalability and extensibility in complex systems   

      2.\ AI-orientated OO patterns (conceptual awareness): briefly note exposure to AI-inspired architectural patterns such            as:   

          - Model Registry (managing lifecycle.versionin of ML models).   

          - Feature Store (centralised, reusable feature management).   

    Design software architectures suitable for large-scale systems, ensuring security and robustness.   

    Develop software solutions that are adaptable for AI models and efficient for data science tasks.   

       -Link to Practical Work:   

        -For each learning objectives, provide examples from your practical work (e.g., coding exercises, case studies,               Capstone Project) that demonstrate your understanding and application of the concepts.    

       
       

                  ******************************************************************    
                  
                  
*1- Secure coding: starting in Unit 7, I used bcrypt hashing to secure an authentication system and I applied a password policy , input validation and limited login attempts. peer`s feedback  after testing my code ,helped me to add username uniqueness check. After that ,I used this in unit 10 to apply TDD in my code.*
 
 *In advance OOP, in unit 2 ,I applied a simple online shopping system using SOLID, and I refactored the code by following the steps.
 In unit 6, I used OOP in built thread safe banking with locks and lock ordering. In unit 11 , I used Dependency  Injection to         decouple UserManager from EmailService.* 

 *Design patterns, in unit 5 after Donald`s feedback I added  set_strategy(), which let one PaymentProcessor switch between            creditcard,crypto and bank transfer during checkout. Also, in unit 8, I moved discount rules into separate strategy classes.         
 In unit 9, in ShopEase I used PaymentStartegy for interchangeable payment methods.*
 
 *In Seminar 4, I built a coffee shop application and I used Decorator to extend objects without changing the, I added milk and        chocolate to a coffee without modifying RegularCoffee. 
 Also, in unit 12 , DiscountDecorator and ShippingDecorator built up the order price step by step.*   
 

 *In unit 12, I applied visitor pattern, which enhance extensibility, because ProductReportVisitor and ProductDiscountVisitor added    reporting operations without editing Product.* *I also applied Abstract Factory in ShopEase ,which supported scalability by creating matching Web and Mobile UI components.*

*2- AI-Oriented Pattern, in my capstone project. I used ModelRegistery that stores model versions and FeatureStore for reusable user feature.*

 *In ShopeEase I used a layered architecture,repository, caching and bcrypt to make the system secure, this feature make the system    suitable for Large-scale architecture.*

 *AI-ready and flexible solutions, RecommendationService relies on  a RecommendationModel interface, in this case the model can be      replaced without changing the service. *

******-------------------------------------------------------------------------------------------------******   

 ### Task2 : Showcase Artefacts:

#### Include Key Artefacts: Include the following artefacts developed during the module:   

1.\ Coding Exercises:   

     -Include your solutions to coding tasks (e.g., thread-safe code in Python, implementation of design patterns).  

2.\ Advanced Design Patterns (Practical): Add artefacts demonstrating:   

      -Strategy Pattern: Interchangable algorithms (e.g., AI decision logic, pricing rules).   

      -Decorator Pattern: Dynamically extending functionality (e.g., logging, security layers).   
  
      -Visitor Pattern: Seperating algorithms from object structures (e.g., analytics/reporting).   

      -Abstract Factory: Family of related objects (e.g., switching AI service providers).   

   For each artefact, describe:    
   Why the pattern was chosen.   
   How it improves maintainability, extensibility or testability.      

3.\ Testing - Mocking and AI-Driven Testing (Practical): Include:  

    -Use of mocking frameworks to:    
       Isolate classes.
       Test AI-dependent components without live models or APIs.    
       
    - Reflection on AI-assisted testing tools:
      Test-case generation.
      Intelligent edge-case discovery.
      Regression testing support.
      Frame testing as supporting OO quality, not replacing engineering judgement.   

4.\ Case Studies/Capstone Project: Briefly highlight:    
     -How design patterns supported scalable architecture.      
     -How testing strategies ensured robustness and reliability.    
     -How AI-readiness was considered at design level (extensibility, abstraction, interfaces).        

5.\ Artefact Description (Critical Commentary): For each artefact, provide a brief description explaining:
    -The object.    
    -Orientated principles and techniques used.     
    -Challenges faced and how you overcame them.     
    
    -Explicitly mention:    
    -Pattern selection trade-offs.     
    -Testing complexity.     
    -Managing abstraction vs over-engineering.     
    
    
                *************************************************************************    
                

  *1/. - In unit 6 : Thread-safe banking system , each account has its own lock. preventing  deadlock by applying transfer acquire locks in consistent order.*    
  

```Python
with first.lock:
    with second.lock:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            account1.balance += amount

```


*In unit 7, password is hashed with bcrypt before storing and duplicate usernames are rejected. Which supported secure authentication.* 

```python 

class User:
    def __init__ (self,username, password):
        self._username=username
        self._password= bcrypt.hashpw(password.encode(),bcrypt.gensalt())
```




*In unit 10, I also used hashed to secure the system.*

```python
class UserManagment:
    def __init__(self, student_id, password,student_email):
        self.student_id = student_id
        self._password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        self._student_email= student_email
```



*Dependency Injection had applied in unit 11, UserManager receives its NotificationService from outside instead of creating EmailService itself.*   


``` python 

class NotificationService(ABC):         #Interface (NotificationService)
    @abstractmethod
    def send_notification(self,user,message):
        pass


class EmailService:
    def send_email(self, user, message):
        print(f"Sending email to {user}: {message}")

class SMSService(NotificationService):                  #Add More Services
    def send_notification(self, user, message):
        print(f"Sending SMS to {user}: {message}")        


class UserManager:
    def __init__(self,notifier:NotificationService):
        self.notifier = notifier

    def register_user(self, user):
        self.notifier.send_notification(user, "Welcome!")
```


*2/.- In unit 5 and 12 I chose Strategy to replace a long if elif chain that violate the Open/Close Principle, I added set_strategy() so the payment method can change during the runtime:*  

```python

processor = PaymentProcessor(CreditCardPayment())
processor.set_strategy(PayPalPayment())

```


*In seminar 4 and unit 12 . I chose Decorator to add features without changing the original class. In ShopEase, decorators build the order price step by step:*

```python
price = DiscountDecorator(BasicOrderPrice(total), 10)
price = ShippingDecorator(price, 20)
```

*I chose Visitor to separate reporting and discount operations from the Product class, so a new report only needs a new visitor class and Product stays unchangable, which improve extensibility.*   

```python 
def accept(self, visitor):
    return visitor.visit_product(self)
```


*I used Abstract Factory in ShopEase, so Web and Mobile UI components considering as matching families.*


*3/.- I used unittest.mock to isolated classes and replace real dependencies:*
```python 
mock_payment = Mock(spec=PaymentStrategy)
mock_payment.pay.return_value = True
order = Order("O001", customer, mock_payment)
assert order.checkout(100) is True
```

*I also mocked Cache and OrderOserver, so checkout and notification were tested without real payment,SMS or email. Because RecommendationService relirs on the RecommendationModel intreface.*


*AI-assisted tool. I used ChatGPT to understand errors and SonarQube to detect code smells.SonarQube flagged some validation code that was logically correct, which supports Lenarduzzi et al.'s (2020) finding that its rules do not always prevent bugs*



*4/.- Capstone Project:*
*making the architecture Scalable by keeping the components loosely coupled within a layered architecture.*


*The ShopEase capstone project uses the Strategy, Decorator, Observer ,Adapter, Visitor and Abstract Factory design patterns to create a scalable and maintainable architecture. These patterns help keep the components **loosely coupled**, allowing individual parts of the system to be changed or extended without significantly affecting other components. The application is organised using a **layered architecture**, separating responsibilities between the domain, repository, service, and application layers.*

*Unit tests checked login, checkout, inventory, decorators and notification, including failure cases such as a wrong password and insufficient stock.*

*ModelRegistry, FeatureStore and the RecommendationModel Interface mean AI models can be replaced or added without rewriting the service.*

*5/.- Critical Commentary:*
*In unit (6), I used encapsulation , kept to the Single Responsibility Principle and used locks. My challenges were how to apply the threads correctly in my code and how to manage multiple threads accessing the same bank account .I read the book(Advanced Python Programming) Nguyen (2022), and I learned to use join() and start() methods .I also used AI to verify the correct implementation and check that the threading was applied correctly. Another issue I faced were a Type Error caused by importing a module instead of class , and threading.thread written in lowercase.. I fixed both by reading the error and working on them.*

*In units 7 and 10 where Secure authentication implemented . I used encapsulation, hashing and TDD. My challenge was that I hadn't installed bcrypt at first, and peer testing exposed the duplicate-username problem. I installed bcrypt and added the missing checks. Also, I used SonarQube to detect the error.*


*ShopEase capstone (Unit 12). I used the four OOP principles, SOLID, Dependency Injection and several patterns. My challenge was combining many patterns in one system. I overcame it by organising the code into layers and services.*

*6/.- Pattern selection trade-offs: In Unit 8, named constants were simpler, but Strategy was more extensible. I learned to choose a pattern only when the system is likely to grow. My peer`s initial post was very helpful and help me to understand the way to start writing my own code.*

*Testing complexity: In unit 10 tests contained typos and wrong assertions, which showed me that tests need the same care as production code.*

*Managing abstraction vs over-engineering: I used AI oriented pattern in simple way as this is the first attempt to apply this pattern.*   



******-------------------------------------------------------------------------------------------------******  
