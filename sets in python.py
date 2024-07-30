#sets in python
#set is mutable but elements inn set is immutable


collection = {1,2,3,4,5,4,9,"hello","world", "hello"}
print(collection)
print(type(collection))
print(len(collection))

#null sets
null_sets = set()
print(type(null_sets))
print(null_sets)

#sets methods:
collection1 = set()
collection1.add(1)
collection1.add(1)
collection1.add(2)
collection1.add(2)
print(collection1)

collection1.remove(1)
print(collection1)

collection1.add("hello")
print(collection1)
collection1.clear()
print(collection1)

collection2 = {"hello", "world", "python"}
print(collection2.pop())
print(collection2.pop())

#intersection and union
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))


