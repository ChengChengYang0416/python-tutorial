#-------------- 1. set --------------#
set1 = {2, 5, 8}
set2 = {1, 2, 3}

# check if the set contains the value
print(2 in set1)
print(1 in set1)
print(1 not in set1)

# 'and' and 'or' of set
set3 = set1&set2
print(set3)
set3 = set1|set2
print(set3)
set3 = set1-set2
print(set3)
set3 = set1^set2
print(set3)

# break down string to set
set4 = set("hello")
print(set4)
#-------------- end of set --------------#


#-------------- 2. dictionary --------------#
dic1 = {"apple":"red", "banana":"yello"}

# modified the value of the key
print(dic1["apple"])
dic1["banana"] = "black"
print(dic1["banana"])

# check if the key in the dictionary
print("apple" in dic1)
print("hello" in dic1)

# delete the key in the dictionary
print("dicitonary before being deleted a key : "),
print(dic1)
del dic1["apple"]
print("dictionary after being deleted a key : "),
print(dic1)

# create a set from a list
dic2 = {i:i*2 for i in [2, 5, 7]}
print(dic2)
print(dic2[2])
#-------------- end of dictionary --------------#