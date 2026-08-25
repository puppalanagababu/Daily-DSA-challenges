
# # Problem 1: Find the Largest Number
# numbers = [12, 45, 8, 67, 23]
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i

# print("Largest:", largest)

# # Problem 2: Find the Smallest Number
# numbers = [15, 8, 23, 4, 90]
# smallest = numbers[0]
# for i in numbers:
#     if i < smallest:
#         smallest = i

# print("Smallest:", smallest)

# # Problem 3: Reverse a String

# text = input("Enter String: ")

# print(text[::-1])

# # Problem 4: Palindrome

# text = input("Enter String: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # Problem 5: Count Even and Odd

# numbers = [10,15,22,31,40,55]

# even = 0
# odd = 0

# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)

# # Problem 6: Sum of List

# numbers = [5,10,15,20]

# total = 0

# for i in numbers:
#     total += i

# print(total)

# # Problem 7: Second Largest

# numbers = [12,45,67,23,89]

# numbers.sort()

# print(numbers[-2])


# # Problem 8: Prime Number

# num = int(input())

# count = 0

# for i in range(1,num+1):
#     if num%i==0:
#         count+=1

# if count==2:
#     print("Prime")
# else:
#     print("Not Prime")

# # Problem 9: Count Vowels

# text = input()

# count = 0

# for i in text.lower():
#     if i in "aeiou":
#         count += 1

# print(count)

# # Problem 10: Remove Duplicates

# numbers = [1,2,2,3,4,4,5,1]

# result = []

# for i in numbers:
#     if i not in result:
#         result.append(i)

# print(result)

# # Problem 11: Linear Search

# numbers = [10,20,30,40,50]

# key = int(input())

# if key in numbers:
#     print(numbers.index(key))
# else:
#     print("Element Not Found")

# # Problem 12: Frequency of Element

# numbers = [1,2,3,2,4,2,5]

# element = int(input())

# print(numbers.count(element))

# # Problem 13: Factorial

# num = int(input())

# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)

# # Problem 14: Fibonacci

# n = int(input())

# a = 0
# b = 1

# for i in range(n):
#     print(a,end=" ")
#     a,b = b,a+b

# # Problem 15: Maximum and Minimum

# numbers = [18,7,45,12,30]

# print(max(numbers))
# print(min(numbers))

# # Problem 16: Count Digits

# num = input()

# print(len(num))


# # Problem 17: Uppercase & Lowercase Count

# text = input()

# upper = 0
# lower = 0

# for i in text:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1

# print("Upper:",upper)
# print("Lower:",lower)

# # Problem 18: Anagram

# a = input()
# b = input()

# if sorted(a)==sorted(b):
#     print("Anagram")
# else:
#     print("Not Anagram")

# # Problem 19: First Non-Repeating Character

# text = input()

# for i in text:
#     if text.count(i)==1:
#         print(i)
#         break

# # Problem 20: Right Triangle Pattern

# for i in range(1,6):
#     print("*"*i)

# # Problem 21: Inverted Pattern

# for i in range(5,0,-1):
#     print("*"*i)

# # Problem 22: Sum of Digits
# num = input()

# total = 0

# for i in num:
#     total += int(i)

# print(total)

# # Problem 23: Reverse Number

# num = input()

# print(num[::-1])

# # Problem 24: Armstrong Number

# num = int(input())

# temp = num

# digits = len(str(num))

# total = 0

# while temp>0:
#     rem = temp%10
#     total += rem**digits
#     temp//=10

# if total==num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# # Problem 25: Character Frequency

# text = input()

# for i in sorted(set(text)):
#     print(i,":",text.count(i))


# # Problem 26: Longest Word

# sentence = input()

# words = sentence.split()

# longest = words[0]

# for i in words:
#     if len(i)>len(longest):
#         longest = i

# print(longest)
