#list
marks = [87, 64, 33, 95, 78]
index1 = marks[0]
print(index1)
print(len(marks))
print(type(marks))

student = ["kaushal", 85, "delhi"]
student1 = student[0]
print(student1)
print(len(student))

#string = immutable(notchange)
#lists = mutable(change)

try:
    str = "hello"
    print(str[0])
    str[0] = y
except:
    print("string doest assign any value to its index")

student2 = ["kaushal", 85, "delhi"]
print(student2[0])
student2[0] = "arjun"
print(student2)

try:
    student3 = ["karan", 95.4, 17, "delhi"]
    print(student[5])
except:
    print("there is no any index of 5")

#slicing
marks2 = [87, 64, 33, 95, 76]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

#list method
list3 = [2, 1, 3]
list3.append(45)
print(list3)
list3.sort()
print(list3)
list3.sort(reverse = True)
print(list3)
list3.reverse()
print(list3)
list3.insert(0,4)
print(list3)
list3.remove(1)
print(list3)
list3.pop(3)
print(list3)

