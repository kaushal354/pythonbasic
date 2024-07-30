#file i/o in python

f = open("file_name", "mode")
mode:-
'r' = reading and write
'w' = open and writing, turncating the file first
'x' = create a new file and open it for write
'a' = open for writing,appending to the end of the file if it FileExistsError
'b' = binary mode
't' = text mode(default)
'+' = open a disk for updating(Reading and writing)

#reading a file 'r'
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close

f = open("demo.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close

f = open("demo.txt","r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close

#writing a file
# it turncate the previous line and write with new if there will not file exists it create an file 
f = open("demo.txt",'w')
f.write("this is a new line")

#overwrite our data

f = open("demo.txt",'w')
f.write("i am learning python")

#append a file
f = open("demo.txt","a")
f.write("i want to become a software engg\n 122")
f.close

r+ = file not turncate overwritefrom existing text read + overwrite
r = file not turncate
w = turncate File
w+ turncate File and write new text
a+ = stream is position at the end of the file read append write a new from starting

f = open("demo.txt","r+")
f.write("abc")
f.close

f = open("demo.txt","w+")
print(f.read())
f.write("abc")
f.close

f = open("demo.txt","a+")
print(f.read())
f.write("abc")
f.close

with open("demo.txt","r") as f:
    print(f.read())

with open("demo.txt", "w") as f:
    f.write("hello ")

#deleting a file(using os module)
import os
os.remove("demo.txt")

practise question file 
1. create a new file "practise.txt" using python. add the following data in it:
hi everyone
we are learning file i/o
using java
i am like programming in java

with open("practise.txt","w") as f:
    f.write("hi everyone\nwe are learning file i/o\nusing java\ni am like programming in java")

#2. replace each occurance of java with python
with open("practise.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

3. search if the word "learning" exist in the file or not
word = "learning"
with open("practise.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

#4. waf to find in which line of the file does the word "learning" occur first
#print -1 if not found
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practise.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_for_line())

#5. from a file containg number sperate by comma, print the count of the even number
# 1,2,45,55,86,76
count = 0
with open("practise.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)




