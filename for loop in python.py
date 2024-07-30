#for loop in python

list = [1,2,3,4,5,6]
for el in list:
    print(el)
else:
    print('end')

veggies = ["potato", "bringal", "ladyfinger", "cucumber"]
for i in veggies:
    print(i)

tup = (1,2,3,4,5,6)
for num in tup:
    print(num)

str = "apnacollege"
for char in str:
    print(char)
else:
    print("end")

str1 = "apna college"
for char1 in str1:
    if(char1 == 'o'):
        print(" o found")
        break
    print(char1)
else:
    print("end")

practicse question from loop
1. print the element of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

#2. search for a number x in this tuple using loop
x = int(input("enter a number :"))
tup = (1,4,9,16,25,36,49,64,81,100)
for i in list:
    if(i == x):
        print("the number",x, "found")
        break
else:
    print("enter number not found")

                        #or for index
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = -1
for el in nums:
    if(el == 36):
        print("the number found at index",idx)
    idx += 1

#range function in for loop

for el in range(11):
    print(el)

print(range(5))

seq = range(5)
print(seq[1])

for i in range(2,10):
    print(i)

for i in range(2,10,2):
    print(i)

#practise questions
#1. print numbers from 1 to 100
for i in range(1,101):
    print(i)

#2. print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#3. multiplication table of number x
nums = int(input("enter a number x: "))
for i in range(1,11):
    print(nums*i)

#pass statement in loop

try:
    for i in loop(100):

        print("hello")
except:
    print("if there is empty it show error")
finally:
    print("that why we use pass statement to solve this problem")

for i in range(5):
    pass

#practise question related to loops
#1. wap program to find sum of first n numbers(using while)
n = int(input("enter a number n: "))
i = 0
a=0
while i <= n:
    a = a + i
    i += 1

print("the sum of num",n, "is :",a)

#2. wap to find the factorial of first n number(using for)
x = int(input("enter a number x"))
a = 1
for i in range(x,1,-1):
    a = a * i

print("the factorial of number",x, "is:", a)


