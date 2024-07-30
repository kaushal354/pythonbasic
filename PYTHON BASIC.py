#basic of python
name = "shradha"
age = 23
price = 25.99
print("my name is :",name,",my age is:", age,",the price of the book is:", price)
print(type(name))
print(type(age))
print(type(price))
old = False
p = None
print(old, p)
print(type(p),type(old))

#print sum
a = 2
b = 5
sum = a + b
print(sum)

#expression execution
#1. this is for string and numeric operator together with *
A,B = 2,3
Txt = "@"
print(A*Txt*B)
#2. String and string operator together
C,D = "2",3
str = "@"
print((C+str)*D)
#3. numeric values can operate with all arthematics operator
E,F = 2,3
G = 4
print(E+F*G)
#4. arthematic expression with ineteger and float will result in float
H,I = 10,5.0
J = H*I
print(J)
#5. Result of division operator with two integer will be floats
K,L = 1,3
M = K/L
print(M)
#6. Integer division with float and int will give int displayed as float
N,O = 1.5,3
P = N//O
print(P,N/O)
#7. Remainder is negative when denominator is negative
Q,R = 5, -2
S = Q%R
print(S)
# #single line comment
"""multi lined comment"""

#input in python
NAME = input("NAME: ")
AGE = int(input("age: "))
PRICE = float(input("price: "))
print(NAME)
print(AGE)
print(PRICE)


