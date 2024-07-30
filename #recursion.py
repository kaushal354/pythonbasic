#recursion (the function call it self repeatadly )
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1) * n

print(fact(5))

def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n



print(sum(5))

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

fruits = ["mango", "litichi","apple", "banana"]
print_list(fruits)

