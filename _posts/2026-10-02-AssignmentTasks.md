---
layout: post
title: AssignmentTasks
subtitle: Journey into advanced OOP concepts
categories: markdown
tags: [Task1️⃣, Task2️⃣ ,Task3️⃣, Task4️⃣ ]
---   

### Task 1️⃣: Summarise Key Learning Outcomes  

     -Reflect on Learning Objectives: Provide a summary of how you have achieved the module’s learning objectives:   

     -Understand and implement secure coding practices in software development.   

     -Apply advanced object – oriented principles to solve complex software problems.   

     -Utilise design patterns to create reusable, maintainable, and flexible code.  

      -Briefly extend your reflection to include:   

        1. Advanced design pattterns (practical application):mention hands-on use of Strategy, Decorator, Visitor and                              Abstract Factory, explicitly linking them to:   

          -Runtime behavioural flexibility.   

         -Seperation of concerns.   

        -Scalability and extensibility in complex systems   

      2. AI-orientated OO patterns (conceptual awareness): briefly note exposure to AI-inspired architectural patterns such                     as:   

          - Model Registry (managing lifecycle.versionin of ML models).   

          - Feature Store (centralised, reusable feature management).   

       Design software architectures suitable for large-scale systems, ensuring security and robustness.   

        Develop software solutions that are adaptable for AI models and efficient for data science tasks.   

           -Link to Practical Work:   

            -For each learning objectives, provide examples from your practical work (e.g., coding exercises, case studies,               Capstone Project) that demonstrate your understanding and application of the concepts.  
            
                  ******************************************************************    
                  
                  
##### 1-Secure coding

* Starting in Unit 7, I used bcrypt hashing to secure an authentication system, and I applied a password policy, input validation, and limited login attempts. peer`s feedback after testing my code helped me to add a username uniqueness check. After that, I used this in Unit 10 to apply TDD in my code.*


#### In advance Object Oriented Principles
 
 *In Unit 2, I refactored a simple online shopping system using the SOLID principles. As a result, the Order class depended on the abstract Payment Method and Discount Method classes rather than on specific implementations.*  
 
*In Unit 6, I developed a thread-safe banking system using locks and lock ordering. This work applied OOP principles and maintained proper encapsulation. In Unit 11, I used dependency injection to separate the User Manager from the Email Service.* 

### Design patterns   

#### Strategy   
 *In Unit 5, based on feedback from my colleague, I added the set_Strategy () method. This method allows the Payment Processor to switch between different payment methods, such as credit card, cryptocurrency, and bank transfer, during checkout. In Unit 8, I separated the discount rules into individual strategy classes. In Unit 9, I applied the Payment Strategy pattern in ShopEase to support interchangeable payment methods.*

#### Decorator  
 *In Seminar 4, I built a coffee shop application, and I used Decorator to extend objects without changing them. I added milk and chocolate to a coffee without modifying RegularCoffee. Also, in Unit 12, Discount Decorator and Shipping Decorator built up the order price step by step.*   
 
#### visitor   
 *In unit 12, I applied the Visitor pattern, which enhanced extensibility, because Product Report Visitor and Product Discount Visitor added reporting operations without editing Product.*     
 
#### Abstract Factory   
 *I also applied Abstract Factory in ShopEase, which supported scalability by creating matching Web and Mobile UI components.*    
 

### 2-AI-Oriented Pattern 

*In my capstone project, I used a Model Registry to store different model versions and a Feature Store to manage reusable user features. Initially, the registry stored only the model’s name as text, so the output did not display any information about the model. I corrected this issue, and the output now shows the model and its version retrieved from the registry.*   

*In ShopEase, I used a layered architecture that includes repositories, caching, and b crypt to improve the system’s security and performance. This design also makes the system suitable for future expansion into a large-scale architecture.*   

*AI-ready and flexible solutions, Recommendation Service relies on a Recommendation Model interface; in this case, the model can be replaced without changing the service.*   
 

******--------------------------------------------------------------------------------------******    


         

### Task 2️⃣ : Showcase Artefacts

    -Include Key Artefacts: Include the following artefacts developed during the module:   

         1. Coding Exercises:   

             -Include your solutions to coding tasks (e.g., thread-safe code in Python, implementation of design patterns).  

         2. Advanced Design Patterns (Practical): Add artefacts demonstrating:   

             -Strategy Pattern: Interchangable algorithms (e.g., AI decision logic, pricing rules).   
  
             -Decorator Pattern: Dynamically extending functionality (e.g., logging, security layers).   
  
             -Visitor Pattern: Seperating algorithms from object structures (e.g., analytics/reporting).   

             -Abstract Factory: Family of related objects (e.g., switching AI service providers).   

                  - For each artefact, describe:    
                  - Why the pattern was chosen.   
                  - How it improves maintainability, extensibility or testability.      

         3. Testing - Mocking and AI-Driven Testing (Practical): Include:  

                Use of mocking frameworks to:    
                   - Isolate classes.
                   - Test AI-dependent components without live models or APIs.    
       
             - Reflection on AI-assisted testing tools:
                 Test-case generation.
                 Intelligent edge-case discovery.
                 Regression testing support.
                 Frame testing as supporting OO quality, not replacing engineering judgement.   
              

        4. Case Studies/Capstone Project: Briefly highlight:    
             -How design patterns supported scalable architecture.      
             -How testing strategies ensured robustness and reliability.    
             -How AI-readiness was considered at design level (extensibility, abstraction, interfaces).   
        

       5. Artefact Description (Critical Commentary): For each artefact, provide a brief description explaining:
            -The object.    
            -Orientated principles and techniques used.     
            -Challenges faced and how you overcame them.     
    
                Explicitly mention:    
                  -Pattern selection trade-offs.     
                  -Testing complexity.     
                  -Managing abstraction vs over-engineering.     
    
    
              *************************************************************************  
                
                
### 1-Coding Exercises    

#### Thread-safe banking system    


  *1\. In unit 6 : Thread-safe banking system , each account has its own lock. preventing  deadlock by applying transfer acquire locks in consistent order.*    
  

```Python
with first.lock:
    with second.lock:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            account1.balance += amount

```

#### Secure authentication     

*In unit 7, the password is hashed with bcrypt before storing and duplicate usernames are rejected. Which supported secure authentication.* 

```python 

class User:
    def __init__ (self,username, password):
        self._username=username
        self._password= bcrypt.hashpw(password.encode(),bcrypt.gensalt())
```



*In unit 10, I also used hashing to secure the system.*

```python
class UserManagment:
    def __init__(self, student_id, password,student_email):
        self.student_id = student_id
        self._password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        self._student_email= student_email
```


#### Dependency Injection   

*Dependency Injection was applied in unit 11; User Manager receives its Notification Service from outside instead of creating Email Service itself.*   


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

### 2-Advanced Design Patterns       

*In unit 5 and 12 , I chose Strategy to replace a long if elif chain that violates the Open/Close Principle, I added set_strategy() so the payment method can change during the runtime:*  

```python

processor = PaymentProcessor(CreditCardPayment())
processor.set_strategy(PayPalPayment())

```


```Python
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Paid ${amount:.2f} using Credit Card" )

        return True


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Paid ${amount:.2f} using PayPal")

        return True


class CashPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Paid ${amount:.2f} using Cash")

        return True
```

#### Decorator  

*In Seminar 4 and Unit 12, the Decorator pattern is explored in order to add new features without changing the original class. In ShopEase, decorators calculate the order price step by step. To this end, each decorator has a single responsibility. This would help to improve the maintainability and management of the system. Noting that new rules for pricing can also be included in the system by simply adding new decorators.*   

##### Seminar 4   

```python
  #Customise the Coffee
coffee = RegularCoffee()                                     

coffee = Milk(coffee)
coffee = ChoclateDuster(coffee)
```


##### Unit 12    

```Python
 #Decorator

    basic_price = BasicOrderPrice(customer.calculate_cart_total() )

    discounted_price = DiscountDecorator(basic_price, 10)

    final_price = ShippingDecorator(discounted_price, 20)

    total = final_price.calculate_price()
```

#### Visitor 

*Visitor is chosen to separate reporting and discount operations from the class of the Product. As such, the new report needs a new visitor class. Therefore, the product stays unchanged, which enhances extensibility.*   

```python 
def accept(self, visitor):
    return visitor.visit_product(self)
```

#### Abstract Factory    

*The Abstract Factory in ShopEase is explored. Therefore, matching families with Web and Mobile UI components are utilized..*     
```PYHTON
class UIButton(ABC):

    @abstractmethod
    def render(self):
        pass


class UIMessage(ABC):

    @abstractmethod
    def display(self, message):
        pass


class WebButton(UIButton):

    def render(self):

        return "Rendering Web Button"


class WebMessage(UIMessage):

    def display(self, message):

        return f"Web Message: {message}"


class MobileButton(UIButton):

    def render(self):

        return "Rendering Mobile Button"


class MobileMessage(UIMessage):

    def display(self, message):

        return f"Mobile Message: {message}"
```


#### 3-Testing: Mocking and AI-Assisted Tools

### Mocking   

*3. I used a unittest.mocked to isolated classes and replace real dependencies:*
```python 
mock_payment = Mock(spec=PaymentStrategy)
mock_payment.pay.return_value = True
order = Order("O001", customer, mock_payment)
assert order.checkout(100) is True
```

*I also mocked Cache and OrderOserver, so checkout and notification were tested without real payment,SMS or email. Because RecommendationService relies on the RecommendationModel intreface.*


#### AI-assisted tools   

*I used ChatGPT to help me understand and fix errors in the code. SonarQube is also used in this report to identify possible code smells. Although SonarQube was logically correct, it flagged some validation code. This discovery agrees with the findings of Lenarduzzi et al. (2020).*



### *4. Capstone Project:*    

#### Scalable architecture     

*The ShopEase capstone project uses several design patterns, including Strategy, Decorator, Observer, Adapter, Visitor, and Abstract Factory. These patterns help create a scalable and maintainable architecture by keeping the system components loosely coupled. This allows individual parts of the system to be changed or extended without having a significant effect on the other components.
The application is organised using a layered architecture that separates responsibilities between the domain, repository, service, and application layers.*

#### Robustness       

*I followed a Test-Driven Development (TDD) based approach. At the beginning, all tests failed with a NameError. This is because the classes under evaluation had not yet been considered, which achieved the red stage of the cycle in TDD. After implementing the required classes, all six tests have passed. By completing these tasks, the green stage is completed. The TDD covers different things, including the login, inventory, management, decorators, checkout recommendations, and notifications.*

#### AI-readiness      

 *This includes the feature store and model registry, as well as the recommendation model Interface. This implies that the AI models can be replaced or added without rewriting the service.*   

### 5- Critical Commentary   

#### Thread-safe banking 
 *In Unit 6, I applied encapsulation, followed the Single Responsibility Principle, and used locks to protect the system. One of the main challenges was applying threads correctly and managing multiple threads accessing the same bank account. After reading Advanced Python Programming by Nguyen (2022), I learned how to use the start () and join() methods.   
I also encountered a TypeError because I imported a module instead of a class. In addition, I wrote threading thread in lowercase instead of using the correct form, threading. Thread. I fixed both problems by carefully reading the error messages and correcting the code.*
    

#### Secure authentication

*In units 7 and 10, secure authentication was implemented. I used encapsulation, hashing, and TDD. My challenge was that I hadn’t installed bcrypt at first, and peer testing exposed the duplicate-username problem. I installed bcrypt and added the missing checks. Also, I used SonarQube to detect the error.*

#### ShopEase capstone   

*ShopEase capstone (Unit 12). I used the four OOP principles, SOLID, Dependency Injection, and several patterns. My challenge was combining many patterns in one system. I overcame it by organising the code into layers and services.*    

### 6- Reflection   

#### Pattern selection trade-offs       

 *In Unit 8, named constants were simpler, but strategy was more extensible. I learned to choose a pattern only when the system is likely to grow. My initial evaluation was very helpful since it helped me to understand the effective way to start writing my own code.*

#### Testing complexity 

*Unit 10 evaluation contained typos and wrong assertions. This shows that the tests need the same consideration as production code.*   

#### Abstraction vs over-engineering 

*Balancing abstraction is done against over-engineering. To this end, I used an AI-oriented pattern in a simple way since this was considered as the first attempt to apply this pattern.*  

******--------------------------------------------------------------------------------------------******    
          

          

### Task 3️⃣: Reflect on Skill Development:

      -Academic Skills: Reflect on how the module has helped you developed critical academic skills such as:   

      -Critical thinking and analysis: How you analysed complex software problems and applied OOP principles to solve them.  
     
      -Ethical considerations in AI-driven OO designs: bias propagation through poorly designed class hierarchies,                             transparency and explainability challenges in AI-enabled objects, responsibility of OO designers in - ensuring                          testability, avoiding "black box" coupling and supporting auditability through clean design.   
     
     
     -Problem-solving: How you approached coding challenges and refactored code to improve maintainability.   
    
     -Research and self-study: How you engaged with reading materials, research papers, and case studies to deepen your                         understanding.   
    
     -Employability Skills: Reflect on how the module has helped you develop key employability skills such as:   

      -Time management: How you managed your time to complete coursework, practical exercises, and the Capstone Project.   
    
      -Communication and literacy: How you communicated your ideas in collaborative discussions and written reports.   
   
      -Resilience and Interpersonal Skills: How you worked through challenges and collaborated with peers in group                              activities.    

             ******************************************************************    
            

### 💡Critical thinking and analysis   

*This module taught me the importance of analysing a problem before writing code. In Unit 5, I identified three design problems in the original Payment Processor: it violated the Open/Closed Principle, was tightly coupled, and used a long if-elif chain. I solved these problems by applying the Strategy pattern.*   

*In Unit 8, I compared two different solutions. I found that using named constants improved readability but did not remove the long method, while the Strategy pattern applied the Open/Closed Principle more effectively. I also learned how to review my peers’ work critically. For example, I explained to Sopheaktra that using a dictionary of discount values did not fully implement the Strategy pattern.*   

*I also learned to evaluate development tools carefully. SonarQube flagged some of my validation code even though it was logically correct. This supported the findings of Lenarduzzi et al. (2020), who stated that SonarQube rules do not always prevent software bugs.*   


### ⚖️ The considerations of ethics in AI design   

*Some groups may be treaded unfairly using the AI model, as explained in Aljawawdeh et al. (2024). The authors also explained that AI is based on black-box models, so that no one can know their decisions. To this end, in OOD, a subclass inherits the rules of its parent class. For example, my Car class inherited from the Vehicle class in Unit 1. This implies that if a parent class contains a biased rule, that bias could affect all of its subclasses.*      

*When separate strategy classes are used, each rule is clearer and easier to evaluate. The work in Unit 11 also showed that the problems can be caused by black-box coupling. The original User Manager was tightly connected to the Email Service, which made it difficult to evaluate because it always attempted to send a real email. In ShopEase, the Recommendation Service depends on the Recommendation Model interface, allowing me to evaluate it with a mock model instead of using a real one.*       

 *The authors also recommend keeping auditable logs of AI decisions. This relates to Donald’s suggestion in Unit 7 to record failed login attempts. I now understand that OOD has a responsibility to create systems that are testable, transparent, and traceable.*  

  
### 🧠 How I learned problem solving technique       

*I have addressed several programming problems and I have faced several coding challenges during my writing the program code. I have  analysed my reading error messages carefully and worked on resolving each error sequentially by solving one problem at a time. Examples are given bellow:   

• *In Unit 2, a NameError function was used in programm, which resulted from using Discount Method before defining it, which resulted in an incorrectly spelling Percentage Discount.*   

• *In Seminar 4, a Type Error occurred because I referred to a method without invoking it, which indicates omitting the parentheses needed to call the method and adding () fixed it.*    

• *In Unit 6, I fixed a Type Error caused by importing the module rather than the class itself, and an Attribute Error caused by writing threading. (thread in lowercase) instead of the correct capitalisation.*    

• *In my capstone, the program was executed successfully without errors but displaying no information about the AI model. Based on using an appropriate  AI tool, I found that Model Registry stored the model's name as text, and I amended this error and fix it.*   


*To enhance maintainability, the code was also refactored. For example, in Unit 7, I refactored an insecure authentication system, and in Unit 8, I moved discount rules into separate strategy classes.*    

####  📚 How I conducted research and self-learning   

*Several books have been considered in my reading. Then, I have applied the concepts in these in my report. Examples of these books are*:
•       Sridhar, Indumathi and Hariharan (2023) for OOP principles.
•      	Sarcar (2022) for SOLID and design patterns, which I used in Units 2, 3 and 4.
•      	Nguyen (2022) for threading.
•      	Baker (2022) for password rules.
•      	Violetta (2023) and Clausen (2021) for refactoring.
•      	Chow (2024) for layered architecture.
•      	Tibi (2022) for TDD.

*Following Dr Nawaz enquiry about the possibility of applying different tools to identify code smells, I reviewed the research work carried out by Lenarduzzi et al. (2020), which led me to install the SonarQube library in VS Code. In addition, a further useful resource that helped me to learn and fix errors was watching YouTube videos. These videos motivated me to understand the Adapter and Bridge patterns in Unit 4 as well as layered architecture in Unit 9, even when the examples were written in JavaScript.*    



### Employability Skills  

#### ⏰Time management   

*I managed my time by preparing for each seminar in advance. For example, I had already covered part of Unit 2 when the tutor asked whether we had heard of SOLID. I also added my work to my e-portfolio one unit at a time, which helped me build up to the capstone project step by step.*   

#### 📝 Communication and literacy      

*I expressed my perspectives by participating in four collaborative discussions. To this end, I posted my initial contributions, considered the feedback that I received, and provided my peers’ contributions based on the feedback that I received. In particular, I provided all the essential comments to all the feedback that I have received, including the feedback that I have obtained from Molly, Kaona, Séba, Reem, and Sopheaktra. I have also provided comments in reply to Donald and Dr Nawaz.*   

*I have attended several seminars during my study course. During these seminars, I presented my work. These seminars include an explanation of concurrency in Seminar 6 and the Red-Green-Refactor cycle in Seminar 8. I have also obtained feedback from my tutor, who provided me with comments on Unit 6. Interestingly, I have received positive feedback from my tutor who observed that my report is well written and well structured. One of the comments was that my report contained clear sections. It is worth noting that I have also explored AI tools in order to assist me with proofreading and to check the grammar and spelling.*


#### 📉📈 Resilience and interpersonal skills   


*Here I discuss how I work hard during my course to improve my resilience and interpersonal skills. I have resolved the errors that I have discovered and the errors that my tutor found without giving up. These errors include threading mistakes in Unit 6, the absence of bcrypt library installation in Unit 7, and the Model Registry problem in my capstone.*   

*Even though there were errors, my peers' initial posts were highly beneficial because reading them motivated me to discover new ideas for writing my own code. Examples of these errors are provided below.*  

• *Reem's Unit 8 post contrasted the simple approach evaluated against the Strategy pattern.*    

• *Séba's Unit 5 post employed set_strategy() to switch payment methods at runtime.*    

• *I found Séba's suggestions in Unit 7 particularly useful.
To this end, Séba's suggestions have been incorporated and applied to my report to refine my code.*   

*On the other hand, Donald has recommended the use of set_strategy() in Unit 5 and Unit 7. Séba identified the duplicate-username problem, and Donald advised logging failed login attempts. This feedback that I have obtained during the course demonstrated that collaboration and teamwork can significantly help in identifying problems that are difficult to observe in individual work.* 


******----------------------------------------------------------------------------------------------******


### Task 4️⃣ : Professional Development Plan (PDP):

        -Identify Strengths and Areas for Improvement:
          -Based on your performance in the module, identify your strengths (e.g., areas where you excelled) and areas for              improvement  (e.g., concepts or skills you found challenging).  
 
        -Future Goals and Actions:   
 
         -Deeping expertise in AI-aware software architecture.
         -Advanced testing strategies for intelligent systems.
         -Ethical software engineering in AI-integrated applications.
         
          ****************************************************************** 


******-------------------------------------------------------------------------------------------------******  
