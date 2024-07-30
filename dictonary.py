#dictonary

dict = {
    "name" : "kaushal",
    "cgpa" : 9.6,
    "marks" : [98,97,95]
}
print(dict)
print(dict["name"], dict["cgpa"], dict ["marks"])
print(type(dict))

dict1 = {
"subjects" : ["python", "c", "java"],
"topics" : ("dict", "set")
}
print(dict1)
print(dict1["subjects"], dict1["topics"])
print(type(dict1["subjects"]))
print(type(dict1))

#null dictonary
null_dict = {} #empty dict
print(null_dict)

null_dict["name"] = "apna college"
print(null_dict)

#nested dictionaries
student = {
    "name" : "students",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 96
    }
}
print(student)
print(student["score"]["math"])

#dictonary method
print(student.keys())
print(len(student.keys()))
print(student.values())
print(len(student.values()))
print(list(student.values()))
print(student.items())
print(tuple(student.items()))
pairs = list(student.items())
print(pairs[0])
print(student["name"])
print(student.get("name"))

try:
    print(student["name2"])
except:
    print(student.get("name2"))
finally:
    print("difference between get and normal is when there\n is no any key there of name2 normal where show error but get running successfully with the value none")

student.update({"city" : "delhi"})
print(student)

new_dict = {"phone.no" : 9661392401}
student.update(new_dict)
print(student)


