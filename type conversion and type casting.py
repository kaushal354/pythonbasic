#type conversion
a,b = 1,2.0
sum = a + b
print(sum)

try:
    c,d = 1,"2"
    type = c + d
    print(type)
except:
    print("there is an error that show str and int not able to add")
finally:
    print("example of type conversion")

#for fixed this type conversion issue we use typecasting
#int(val) , float(val), str(val)
e,f,h = 1,"2",int("3")
g = int(f)
typecasting = e + g + h
print(typecasting)
print(type(g))
print(type(h))

i = 3.14
string = str(i)
print(type(string))





