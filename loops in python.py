# loops in python
# while ,for

while True:
    print("hello") #infinite loop

count = 1
while count <= 5:
    print("hello")
    count +=1

i = 5
while i >= 1:
    print(i)
    i -= 1

print("loop ended")

#practicse question from while loop
#1. print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i +=1

#2. print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# 3. print multiplication table of a number n

n = int(input("enter a number n: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# 4. print the elements of the following list using a loop:
#1,4,9,16,25,36,49,64,81,100

nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while  idx < len(nums):
    print(nums[idx])
    idx += 1

# 5. search for the element a number x in this tuple using loop:
# nums1 = (1,4,9,16,25,36,49,64,81,100)

x = int(input("enter a number:-"))

idx = 0
while idx < len(nums1):
    if (nums1[idx] == x):
        print("number found at index:", idx)
    else:
        print("searching")
    idx += 1

#break and continue
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1

i = 0
while i <= 5:
    if(i==3):
        i += 1
        continue
    print(i)
    i += 1
