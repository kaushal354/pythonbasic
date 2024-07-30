#oops in python2
#inheritance 
#when one class (child/divered) derived the properties & methods of another class(parent/base):

class car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")

class Toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")
print(car1.start())

#type of inheritance:
#1. single inheritance :- one parent class and drived into one child class
#2. multi-level inheritance :- one parents class and drived into multiple child class
#3. multiple inheritance :- two parents class and drived to one child class

#single inheritance and multi-level inheritance
class car1:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class Toyotacar(car1):
    def __init__(self,brand):
        self.brand = brand

class fortuner(car1):
    def __init__(self,type):
        self.type = type

car1 = fortuner("disel")
car1.start()

#multiple inheritance 
class A:
    varA  = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method:
#super method is used to access methods of the parents class

class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped")

class ToytaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToytaCar("prius","electric")
print(car1.type)

#class method
#a class method is bound to the class and receive the class as an impliciet first argument
#static method can't access or modify class state & genrally for utility

class person:
    name = "anonymous"
    
    @classmethod
    def change(cls,name):
        cls.name = name

p1 = person()
p1.change("rahul kumar")
print(p1.name)
print(person.name)

#property 
#we use @ property decorator on method in the class to use the as a property
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu = student(98,97,99)
print(stu.percentage)

stu.phy = 86
print(stu.phy)
print(stu.percentage)

#to solve this issue of modifying we use @property 
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu = student(98,97,99)
print(stu.percentage)

stu.phy = 86
print(stu.phy)
print(stu.percentage)

# @getattr
# @setattr

#polymorphism : operator overloading
#when the same operator is allowed to have different meaning according to the context
#operator & dunder function:-
#a+b a.__add__(b)
#a-b a.__sub__(b)
#a*b a.__mul__(b)
#a/b a.__truediv__(b)
#a%b a.__mod__(b)

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i+", self.img,"j")
    
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal,newimg)

num1 = complex(1,3)
num1.shownumber()

num2 = complex(4,6)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

#practicse oops concept
#1.define a circle class to create a circle with radius r using the constructor define an area() method of the class which calculates the area 
#of the circle define perimentet() method of the class allow you to calculate teh perimeter of a circle

class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

ap1 = circle(4)
print(ap1.area())
print(ap1.perimeter())

#2. define employee class with attributes role,department and salary this class also have show details() method
#create an engineer class that inherit properties from employee & and additional attributes :name and age
class employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("role",self.role)
        print("department",self.department)
        print("salary",self.salary)

class engineer(employee):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT","75000")

engg1 = engineer("elon musk",40)
engg1.showdetails()

3.create a class called order which stores item & its price
use dunder function __gt__() to convey that order1>order2 if price of order1 > price of order 2

class order:
    def __init__(self,item,price):
        self.price = price
        self.item = item

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = order("chips",20)
odr2 = order("tea",15)
print(odr1 > odr2)



