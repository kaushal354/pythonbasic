#string
str1 = "hello"
str2 = "world"
final_str = str1 + str2
print(final_str)

len1 = len(str1)
print(len1)

str3 = "this is a string"
str4 = 'apna \t college'
str5 = """this is\n string"""
print(str3, str4, str5)

str6 = "apna"
str7 = "college"
final_str1 = str1 + " " + str2
print(final_str1)
print(len(final_str1))

#indexing

str8 = "apna college"
ch = str8[0]
print(ch)

try:
    str[4] = "@"
except:
    print("we are not able to assign value to string index")
finally:
    print("indexing")

#slicing
str9 = "apna college"
print(str9[1:4])
print(str9[:4])
print(str9[1:])
print(str9[5:len(str9)])

#negative slicing
str10 = "apple"
print(str10[-3:-1])

#string functipn
str11 = "i am a coder"
print(str11.endswith("er"))
print(str11.capitalize())
print(str11.replace("a","o"))
print(str11.find("a"))
print(str11.count("o"))



