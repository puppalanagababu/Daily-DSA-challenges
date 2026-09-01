#1 Print all elements of an array

arr = [10, 20, 30, 40, 50]

for num in arr:
    print(num)

#2 Find the largest element
arr = [10, 20, 30, 40, 50]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(largest)

#3. Find the second largest element
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

# Today's 3 concepts
# Problem	              What you learn
# Print elements	      Array traversal
# Largest element	      Compare with max
# Second largest	      Maintain 2 variables