#practise question from dict and sets

""" 1.store following word meaning in a python dictornary
table : "a piece of furniture ", "list of fact & figure"
cat :"a small animal' """

dict = {
    "tuple" : ["a piece of furniture", "list of fact & figure"],
    "cat" : "a small animal"
}
print(dict)

"""2. you are given a list of subjects for students. assume one classroom is required for 1 subject how many classroom are needed by all students  """
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "python", "java", "c++","c"}
print("total class required for each subject in class", len(subjects))

"""3. wap to enter marks of 3 subjects from the users and store them in a dictornary. start with an empty dictonary & add one by one use subject name as key & marks as value """
subject = {}
phy = int(input("enter a marks of a phy: "))
chem = int(input("enter a marks of chem: "))
math = int(input("enter a marks of maths: "))
subject.update({"physics" : phy})
subject.update({"chemistry" : chem})
subject.update({"mathematics" : math})
print(subject)

"""4. figure out a way to store 9 and 9.0 as a sperate values in set"""
set = {9, "9.0"}
print(set)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)