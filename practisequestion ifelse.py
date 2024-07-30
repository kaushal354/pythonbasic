#wap to input 2 int number  a and b print true if a is greater than or equal to b if not print false
a = int(input("enter a first number:- "))
b = int(input("enter a second number:- "))
if a >= b:
    print(True)
else:
    print(False)

#wap to check if a number entered by the user is odd or even
num = int(input("enter a number:- "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#wap to find the greatest of a 3 numbers entered by the users
num1 = int(input("enter a first number:- "))
num2 = int(input("enter a second number:- "))
num3 = int(input("enter a third number:- "))
if num1 > num2 and num2 > num3:
    print("num1 is greater")
elif num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")

#wap to check number is a multiple of 7 or not
num4 = int(input("enter a num:-"))
if num4 % 7 == 0:
    print("it is divible by 7")
else
