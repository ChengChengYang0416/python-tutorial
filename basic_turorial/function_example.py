#-------------- 1. function --------------#
# declare a function
def add_two_num(n1, n2):
    sum = n1 + n2
    return sum

def calculate(max):
    sum = 0
    for n in range(max+1):
        sum += n
    print(sum)

# call the function
value = add_two_num(5, 6)
print(value)

calculate(11)
#-------------- end of function --------------#


#-------------- 2. parameters in function --------------#
def divide(n1, n2):
    result = n1/n2
    print(result)
divide(2, 4)
divide(n2 = 2, n1 = 4)

def print_msgs(*msgs):
    for msg in msgs:
        print(msg)
print_msgs("hello", "world", "python")

def average(*num):
    sum = 0
    for n in num:
        sum += n
    print(sum/len(num))

average(2, 5, 6)
#-------------- end of parameters in function --------------#