#-------------- 1. break --------------#
n = 0
while n < 5:
    if n == 3:
        break
    print(n)
    n+=1
print("The last n is ", n)
#-------------- end of break --------------#


#-------------- 2. continue --------------#
n = 0
for x in [0, 1, 2, 3]:
    if x%2 == 0:
        continue
    print(x)
    n+=1
print("The last n is ", n)
#-------------- end of continue --------------#


#-------------- 3. else --------------#
sum = 0
for n in range(11):
    sum += n
else:
    print(sum)
#-------------- end of else --------------#


#-------------- 4. example --------------#
n = input("Please enter a integer : ")
n = int(n)
for i in range(n):
    if i*i == n:
        print("The square root of ", n, "is", i)
        break
else:
    print("No integer square root.")
#-------------- end of example --------------#