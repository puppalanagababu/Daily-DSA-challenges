# # # 1. Student Class with Attributes & Methods

# # class Student:
# #     def __init__(self, name, roll_no, marks):
# #         self.name = name        #Attribute: stores name
# #         self.roll_no = roll_no  #Attribute: stores roll_no
# #         self.marks = marks      #Attribute: stores marks

# #     def display(self):

# #         print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

# #     def get_grade(self):
# #         if self.marks >= 90:
# #             return "A"
# #         elif self.marks >= 75:
# #             return "B"
# #         else:
# #             return "C"

# # # Creating objects
# # s1 = Student("Anitha", 101, 92)
# # s2 = Student("Ravi", 102, 78)
# # s1.display()
# # s2.display()




# # # 2. Single Inheritance (Animal and Dog)

# #Concept: Dog (child) inherits all properties/methods from Animal (parent).

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def sound(self):
#         print(f"{self.name} makes a sound.")

# class Dog(Animal): # Dog inherits from Animal

#     def bark(self):
#         print(f"{self.name} is barking.")

# d = Dog("Tommy")
# d.eat()
# d.sound()         # inherited method
# d.bark()        # Dog's own method


# # # # 3. Method Overriding in a Child Class

# # # Concept: Child class redefines a method that already exists in Parent class.

# # # class Animal:
# # #     def sound(self):
# # #         print("This animal makes some sound.")

# # # class Dog(Animal):
# # #     def sound(self): # Overriding the parent method
# # #         print("The dog barks.")

# # # class Cat(Animal):
# # #     def sound(self): # Overriding the parent method
# # #         print("The cat meows.")

# # # a = Animal()
# # # d = Dog()
# # # c = Cat()
# # # a.sound()
# # # d.sound()
# # # c.sound()


# # # # 4. Abstract Class Shape (Circle & Rectangle)

# # # Concept: Abstract class defines a blueprint that child classes MUST follow.

# # # from abc import ABC, abstractmethod
# # # import math

# # # class Shape(ABC):
# # #     @abstractmethod
# # #     def area(self):
# # #         pass  # Every shape must implement its own area formula

# # # class Circle(Shape):
# # #     def __init__(self, radius):
# # #         self.radius = radius

# # #     def area(self):
# # #         return math.pi * (self.radius ** 2)

# # # class Rectangle(Shape):
# # #     def __init__(self, width, height):
# # #         self.width = width
# # #         self.height = height

# # #     def area(self):
# # #         return self.width * self.height


# #  # 5. Encapsulation using BankAccount

# # # # Concept: Private attributes starting with '__' cannot be changed directly from outside.

# # # class BankAccount:
# # #     def __init__(self, owner, balance=0):
# # #         self.owner = owner
# # #         self.__balance = balance # private attribute

# # #     def deposit(self, amount):
# # #         if amount > 0:
# # #             self.__balance += amount
# # #             print(f"Deposited {amount}. New balance: {self.__balance}")
# # #         else:
# # #             print("Deposit amount must be positive.")

# # #     def withdraw(self, amount):
# # #         if amount > self.__balance:
# # #             print("Insufficient balance.")
# # #         elif amount <= 0:
# # #             print("Withdrawal amount must be positive.")
# # #         else:
# # #             self.__balance -= amount
# # #             print(f"Withdrew {amount}. New balance: {self.__balance}")
            
# # #     def get_balance(self): # controlled access to private data
# # #         return self.__balance

# # # acc = BankAccount("Meena", 1000)
# # # acc.deposit(500)
# # # acc.withdraw(300)
# # # print("Final balance:", acc.get_balance())

# # # print(acc.__balance) # AttributeError: cannot access private attribute directly



# #  # 6. Multiple Inheritance (Two Parent Classes)

# # # # Concept: A single child class inherits from multiple parent classes.

# # # class Father:
# # #     def skills(self):
# # #         print("Father: Can drive a car.")

# # # class Mother:
# # #     def skills(self):
# # #         print("Mother: Can cook well.")

# # # class Child(Father, Mother): # inherits from both Father and Mother
# # #     def skills(self):
# # #         Father.skills(self)
# # #         Mother.skills(self)
# # #         print("Child: Can code in Python.")

# # # c = Child()
# # # c.skills()


# # # # 7. Class Variables vs Instance Variables

# # # # Concept:
# # # # - Class Variable: Shared by ALL instances.
# # # # - Instance Variable: Unique to EACH object instance.


# # # class SchoolStudent:
# # #     school_name = "Sunrise High"  # Class Variable (Shared by everyone)

# # #     def __init__(self, name):
# # #         self.name = name          # Instance Variable (Unique per student)

# # # s1 = SchoolStudent("Bob")
# # # s2 = SchoolStudent("Charlie")

# # # print(s1.name, "goes to", s1.school_name)  
# # # print(s2.name, "goes to", s2.school_name)  



# # # # 8. Static Method and Class Method

# # # class MathUtils:
# # #     category = "Mathematics"

# # #     @classmethod
# # #     def get_category(cls):  # Receives 'cls' as first argument
# # #         return f"Category: {cls.category}"

# # #     @staticmethod
# # #     def add(a, b):          # Self-contained helper method
# # #         return a + b

# # # print(MathUtils.get_category())  
# # # print(MathUtils.add(10, 20))     



# # # # 9. Polymorphism with Payment Methods

# # # class CreditCardPayment:
# # #     def pay(self, amount):
# # #         print(f"Paid {amount} using Credit Card.")

# # # class PayPalPayment:
# # #     def pay(self, amount):
# # #         print(f"Paid {amount} using PayPal.")

# # # class UPIPayment:
# # #     def pay(self, amount):
# # #         print(f"Paid {amount} using UPI.")

# # # def execute_payment(payment_method, amount):
# # #     payment_method.pay(amount)  # Works for any payment method object

# # # execute_payment(CreditCardPayment(), 100) 
# # # execute_payment(PayPalPayment(), 50)       
# # # execute_payment(UPIPayment(), 30)          



# # # 10. Print Method Resolution Order (MRO)

# # # # Concept: MRO shows the exact search path Python follows for methods in inheritance.

# # class A: 
# #     pass
# # class B(A): 
# #     pass
# # class C(A): 
# #     pass
# # class D(B, C): 
# #     pass

# # print(D.mro())



class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('Ainmal speak')

class Dog(Animal):
    def speak(self):
        print('Dog barks')
d=Dog('Buddy')
d.speak()