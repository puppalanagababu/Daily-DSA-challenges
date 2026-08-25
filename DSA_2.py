# numbers = [10, 5, 8, 20, 15]
# largest = numbers[0]
# second_largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
# for i in numbers:
#     if i > second_largest and i < largest:
#         second_largest = i
# if second_largest == largest:
#     print("No second largest number")
# else:
#     print("Second largest:", second_largest)

num = [10, 5, 20, 8, 12, 18]
a=num[0]
b=num[0]
for i in num:
    if i > a:
        a=i
for i in num:
    if i > b and i < a:
        b=i
if b==a:
    print("No second largest number")
else:
    print("Second largest:", b)



# Concept: Mutable vs Immutable in Python

# Immutable = cannot be changed after it is created
# Mutable   = can be changed after it is created

# Immutable types:
# int     -->  a = 10       (cannot change 10 itself)
# float   -->  a = 3.14
# str     -->  a = "hello"  (cannot change letters)
# tuple   -->  a = (1,2,3)  (cannot add or remove)

# Mutable types:

# list    -->  a = [1,2,3]  (can add, remove, change)
# set     -->  a = {1,2,3}  (can add, remove)
# dict    -->  a = {"x":1}  (can add, remove, change)


a = [10, 20, 30]
b = a            # b and a point to the SAME list
b.append(40)

print(a)         # [10, 20, 30, 40]
print(b)         # [10, 20, 30, 40]

# Why same output?
# because b = a does NOT copy the list
# both a and b point to the same memory location
# so changing b also changes a

# How to make an independent copy?

a = [10, 20, 30]
b = a.copy()     # now b is a separate copy
b.append(40)

print(a)         # [10, 20, 30]      --> not changed
print(b)         # [10, 20, 30, 40]  --> only b changed


# Debugging Challenge 

# Wrong Code:
numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(1, len(numbers)):   # starts from index 1, skips index 0
    total = total + numbers[i]
print("Total:", total)             # gives 140, but expected 150

# What is the Error?
# range(1, len(numbers)) starts from 1
# so numbers[0] which is 10 is skipped
# that is why we get 140 instead of 150

# Fixed Code:
numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(0, len(numbers)):   # start from 0, include all elements
    total = total + numbers[i]
print("Total:", total)             # now gives 150
