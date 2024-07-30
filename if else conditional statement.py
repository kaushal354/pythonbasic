#traffic light code
light = input("enter the color of the traffic light: ")
if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("WAIT")
elif(light == "green"):
    print("GO")
else:
    print("incorrect color choose")

#grade of the student
phy = int(input("enter a physics marks: "))
chem = int(input("enter a chemistry marks: "))
math = int(input("enter a math marks: "))
marks = (phy + chem + math) / 3
print ("the percentage of student",marks)
if marks >= 90:
    print("the grade is A+")
elif marks >= 80 and marks <= 89:
    print("the grade is A")
elif marks >= 70 and marks <= 79:
    print("the grade is B")
elif marks >= 60 and marks <= 69:
    print("the grade is C")
elif marks >=50 and marks <=59:
    print("the grade is D")
else:
    print("the student become fail")

#ternary operator
food = input("food: ")
eat = "YES" if food == "cake" else "no"
print(eat)

#ternary operator
food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("no sweet")

age = int(input("age: "))
vote = ("yes", "no") [age<=18]
print(vote)

sal = float(input("salary :"))
tax = sal*(0.1,0.2) [sal <= 50000]
print(tax)
