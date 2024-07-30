#question related to list and tuple
#wap to ask the user to enter names of their 3 favorite movis & store them in the list
list = []
mov1 = input("enter a first movie name:")
list.append(mov1)
mov2 = input("enter a second movie name:")
list.append(mov2)
mov3 = input("enter a third movie name:")
list.append(mov3)
print(list)

#write a program to check  if a list contains a palindome or not use(copy) method
list1 = [1,2,3,2,1]

x = list1.copy()
list1.reverse()

if x == list1:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#wap to count the number of students with the "a" grade in the following
tuple = ("C", "D", "A", "A", "B","B", "A")
y = tuple.count("A")
print(y)

#store the above value in a list & sort them from "a" to "d"
list2 = ["C", "D", "A", "A", "B","B", "A"]
list2.sort()
#we can't directly print and store it in the var
print(list2)




