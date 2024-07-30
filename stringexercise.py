#wap to input users first name & print its length
str1 = input("enter a first name:- ")
print(len(str1))
                            #or
len1 = len(str1)
print(len1)

#wap to find the occurance of '$' in a string
str2 = "$"
print(str2.find("$"))

#wap to find greater of 4 number (take input from user)
num1 = int(input("enter a first num: "))
num2 = int(input("enter a second number: "))
num3 = int(input("enter a third number: "))
num4 = int(input("enter a fourth number: "))
if num1 > num2 and num2 > num3 and num3 > num4:
    print("first number is greatest")
elif num2 > num3 and num3 > num4:
    print("second number is greatest")
elif num3 > num4:
    print("third number is greatest")
else:
    print("fourth number is greatest")