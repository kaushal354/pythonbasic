#tuple
tup = (87,64,33,95,76)
print(tup[0])
print(tup[1])
try:
    tup[0] = 43
    print(tup)
except:
    print("not allowed in python")

print(type(tup))

#empty tuple
tup1 = ()
print(tup1)

tup2 = (1,)
print(type(tup2))

tup3 = (1)
print(type(tup3))

tup4 = ("0.3")
print(type(tup4))

#slicing in tuple
tup5 = (1,2,3,4)
print(tup5[2:3])
print(tup5[1:])
print(tup5[:3])
print(tup5[1:len(tup5)])

#tuple method
tup6 = (2,1,3,1)
print(tup6.index(3))
print(tup6.count(1))

