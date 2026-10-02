---
layout: post
title: AssignmentTasks
subtitle: Journey into advanced OOP concepts
categories: markdown
tags: [Task1, Task2 ,Task3, Task4 ]
---   

Task1: Summarise Key Learning Outcomes:   


Reflect on Learning Objectives: Provide a summary of how you have achieved the module’s learning objectives:   

Understand and implement secure coding practices in software development.   

Apply advanced object – oriented principles to solve complex software problems.   

Utilise design patterns to create reusable, maintainable, and flexible code.  

Briefly extend your reflection to include:   

Advanced design pattterns (practical application):mention hands-on use of Strategy, Decorator, Visitor and Abstract Factory, explicitly linking them to:   

Runtime behavioural flexibility.   

Seperation of concerns.   

Scalability and extensibility in complex systems   

AI-orientated OO patterns (conceptual awareness): briefly note exposure to AI-inspired architectural patterns such as:   

Model Registry (managing lifecycle.versionin of ML models).   

Feature Store (centralised, reusable feature management).   

Design software architectures suitable for large-scale systems, ensuring security and robustness.   

Develop software solutions that are adaptable for AI models and efficient for data science tasks.   

Link to Practical Work:   

For each learning objectives, provide examples from your practical work (e.g., coding exercises, case studies, Capstone Project) that demonstrate your understanding and application of the concepts.   


*1.\Secure coding: starting in Unit 7, I used bcrypt hashing to secure an authentication system and I applied a password policy , input validation and limited login attempts. peer`s feedback  after testing my code ,helped me to add username uniqueness check. After that ,I used this in unit 10 to apply TDD in my code.
 
In advance OOP, in unit 2 ,I applied a simple online shopping system using SOLID, and I refactored the code by following the steps.
In unit 6, I used OOP in built thread safe banking with locks and lock ordering. In unit 11 , I used Dependency  Injection to decouple UserManager from EmailService. 


Design patterns, in unit 5 after Donald`s feedback I added  set_strategy(), which let one PaymentProcessor switch between creditcard,crypto and bank transfer during checkout. Also, in unit 8, I moved discount rules into separate strategy classes.
In unit 9, in ShopEase I used PaymentStartegy for interchangeable payment methods. 
 
In Seminar 4, I built a coffee shop application and I used Decorator to extend objects without changing the, I added milk and chocolate to a coffee without modifying RegularCoffee. 
Also, in unit 12 , DiscountDecorator and ShippingDecorator built up the order price step by step.

In unit 12, I applied visitor pattern, which enhance extensibility, because ProductReportVisitor and ProductDiscountVisitor added reporting operations without editing Product.

AI-Oriented Pattern, in my capstone project. I used ModelRegistery that stores model versions and FeatureStore for reusable user feature.

In ShopeEase I used a layered architecture,repository, caching and bcrypt to make the system secure, this feature make the system suitable for Large-scale architecture. 

AI-ready and flexible solutions, 
RecommendationService relies on  a RecommendationModel interface, in this case the model can be replaced without changing the service. *
