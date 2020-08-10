#-------------- 1. usage of list --------------#
# declare a list
num_list = [1, 3, 5, 2, 8, 9]
print(num_list)

# get elements in a list
num = num_list[3]
print(num)

# assign valus in a list
num_list[0] = 0
print(num_list)

# get a piece of elements in a list
num_piece = num_list[1:4]
print(num_piece)

# delete elements in a list
num_list[1:4] = []
print(num_list)

# add elements to a list
num_list = num_list + [2, 6]
print(num_list)
num_list.append(7)
print(num_list)
num_list.insert(2, 5)
print(num_list)

# get length of a list
print(len(num_list))

# 2-d list
list_2d = [[1, 3, 2], [5, 0, 3, 4]]
print(list_2d)
#-------------- end of usage of list --------------#


#-------------- 2. difference between list and tuple --------------#
data_list = ["taipei", "hsinchu", "tainan"]
data_tuple = ("taipei", "hsinchu", "tainan")

# print data stored in list and tuple and the data type
print(data_list)
print(data_tuple)
print(type(data_list))
print(type(data_tuple))

# mutable v.s. immutable
# we can change the values of a list, but we can't change the values of a tuple
city = ["taipei", "hsinchu", "tainan"]
print
print("before changing the element in list : ")
print(city)
city[0] = "taoyuan"     # we can't assign the item like this in tuple
print("after changing the element in list : ")
print(city)

# size difference
# pythone allocates smaller memory to the tuple, which makes tuples faster than list
print
print(data_list.__sizeof__())
print(data_tuple.__sizeof__())
#-------------- end of difference between list and tuple --------------#