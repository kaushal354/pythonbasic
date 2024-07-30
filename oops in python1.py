#oops in python
"""to map with real world scenarios, we started using object in code this is called object oriented programming"""
#class and object
#class is a blueprint for creating objects and objects is instance of class
#creating class
class student: #class
    name = "kaushal"

s1 = student() #object
print(s1.name)

class car:
    color = "blue"
    brand = "mercedes"

car1 = car()
print(car1.color)
print(car1.brand)

#constructor :
#all class have a functipn called __init__(), which always excuted when the class and object is being initiated
class student1:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database..")

s2 = student1("karan")
print(s2.name)
s2 = student1("kaushal")
print(s2.name)

class student2:
    name = "kaushal"
    def __init__(self):
        print("adding new student in database..")

student2()

class student4:
    def __init__(self):#default constructor
                pass 
    def __init__(self,name,marks): #parameterized constructor
        self.name = name
        self.marks = marks
        print("adding new data to data database..")

s4 = student4("komal", 98)
print(s4.name,s4.marks)

s4 = student4("shaurya", 96)
print(s4.name,s4.marks)



#class and instance attributes:
#class.attr
#obj.attr
class student5:
    college_name = "abc college" #class attr
    name = "anomyous"
    def __init__(self,name,marks):
        self.name = name #obj attr >class attr
        self.marks = marks
        print("adding new data to data database..")

s5 = student5("komal", 98)
print(s5.name,s5.marks)

s5 = student5("shaurya", 96)
print(s5.name,s5.marks)

print(student5.college_name)

methods in oops:
method are function that belong to object

class personal:
    def __init__(self,fullname):
        self.name = fullname

    def hello(self):
        print("hello",self.name)

p1 = personal("kaushal")
p1.hello()

class student6:
    college_name = "abc college"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome student",self.name)
    
    def get_marks(self):
        return self.marks

s6 = student6("karan",97)
s6.welcome()
print(s6.get_marks())

#practise question
#1. create student class that takes name & marks of 3 subjects as arguments in constructor. then create a method to print the avg

class student7:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
            avg = sum / 3
        print("hi",self.name,"your avg score is:",avg)

s1 = student7("kaushal",[99,98,97])
s1.avg_marks()

#static method:
"""method that don't use the self parameter (work at class level) it is denoted by @static method which is known as decorator
decorator allows us to wrap another function in order to extends the behviour of the wrapped function, without permanently modyifing it"""

class car1:
    @staticmethod
    def college():
        print("abc college")

#important pillers of oops:
"""1. abstration 
2. encapsulation
3. inhertance 
4. polymorphism"""

#1. abstraction :- hiding the implementation details of a class and only showing the essential information feature to the user
class car2:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("carstarted...")

car1 = car2()
car1.start()

#2. encapsulation :- wrapping data and function into a single unit(object)

#practicse question from abstratcion and encapsulation
#1. create account class with 2 attributes balance & account no create methods for debit, credit & printing the class
class account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance -= amount
        print("rs.",amount,"was debited")
        print("total balance=",self.get_balance())
        print("to account no:",self.get_acc_number())

    def credit(self,amount):
        self.balance += amount
        print("rs.",amount,"was credited")
        print("total balance=",self.get_balance())
        print("to account no:",self.get_acc_number())

    def get_balance(self):
        return self.balance
    
    def get_acc_number(self):
        return self.account_no

acc1 = account(10000,12345)
acc1.debit(1000)
acc1.credit(500000)

#del keywords
#used to delete object properties or object itself

class student10:
    def __init__(self,name):
        self.name = name

s10 = student10("shardha")
print(s10.name)
del s10.name
try:
    print(s10.name)
except:
    print("it show error becuase name already deleted")

private (like) attributes & method:
concepetual implementation in python private attributes & method are meannt to be used only within the class and are not accessible from outside
the class

class account3:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
acc1 = account3("12345","abcde")
print(acc1.acc_no)
try:
    print(acc1.acc_pass)
except:
    print("acc_pass is not showing because it is in private attributes")
finally:
    print("we can print it by using new method show that we access the password")

class account3:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = account3("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())

try:
    class person:
        __name = "anonymous"

    p1 = person()
    print(p1.__name)
except:
    print("it showing error because we can private an attributes")

try:
    class person:
        __name = "anonyomous"

        def __hello():
            print("hello person!")

    p1 = person()
    print(p1.__hello())
except:
    print("it showing error because method and attributes both is private")

class person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())












