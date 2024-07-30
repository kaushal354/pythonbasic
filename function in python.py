#function in python

def sum(a,b): #a,b is a parameter
    s = a+b
    return s

a = sum(9,6) #9,6 is argument
print(a)

def print_hello():
    print("hello")

print_hello()

output = print_hello()
print(output)

def avg_three(a,b,c):
    d = (a + b + c) / 3
    return d

f = avg_three(2,3,4)
print(f)

function is of two type builtin function and user define functipn

#default parameter
def cal_prod(a,b):
    print(a*b)
    return a*b

try:
    m = cal_prod()
    print(m)
except:
    print("it show error because we did't pass any arrguments to a and b parameter")

try:
    n = call_prod(1)
    print(n)
except:
    print("it show error because we write the argument in first parameter but we also want in b parameter")

def cal1(a=4,b=9):
    return a*b

a = cal1()
print(a)

def cal2(c,d=2):
    return c*d

print(cal2(1))

lets practise
#1. waf to print the length of a list (list is a parameter)
nums = [1,2,3,4,5]
def length1(nums):
    a = len(nums)
    return a

b = length1(nums)
print(b)

#2. waf to print the element of a list in a single line list the parameter
nums1 = [1,2,3,4,5]
def sing(nums1):
    for i in nums1:
        print(i, end = " ")

g = sing(nums1)
print(g)

#3. waf to find factorial of n(n is a parameter)
n = int(input("enter a number n:-"))
def factorial(n):
    b = 1
    for i in range(n,1,-1):
        b = b * i
    return b

fact1 = factorial(n)
print(fact1)

#4 waf to convert usd to inr
def mc(usd):
    inr = usd * 83
    return inr

inr1 = mc(96)
print(inr1)

#5. waf take input from user if it is odd return odd if it is even return even
l = int(input("enter a number"))
def evenodd(l):
    if(l % 2 == 0):
        return "even"
    else:
        return  "odd"

evenodd1 = evenodd(l)
print(evenodd1)