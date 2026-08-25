# # my_str = input("Enter a string: ")

# # freq = {}

# # for char in my_str:
# #     if char in freq:
# #         freq[char] = freq[char] + 1
# #     else:
# #         freq[char] = 1

# # for char in my_str:
# #     if freq[char] == 1:
# #         print("First non-repeating character:", char)
# #         break
# # else:
# #     print("No non-repeating character found")


# # # students = ["Ravi", "Anil", "Kiran", "Suresh"]
# # # for student in students:
# # #     if student == "Kiran":
# # #         print("student found :",student)
# # #         break
# # #     else:
# # #         print("student not found")






# # my_str = "goOgle"
# # out = {}
# # for char in my_str:
# #     if char in out:
# #         out[char]+=1
# #     else:
# #         out[char]=1
# # print(out)
# # for s in out:
# #     if out[s]==1:
# #         print("the first non repeating charater is",s)
# #     else:
# #         ("all are repeating characters")


# # my_str = "programming"
# # out = {}
# # for char in my_str:
# #     if char in out:
# #         out[char]+=1
# #     else:
# #         out[char]=1
# # print(out)
# # for s in out:
# #     if out[s]==1:
# #         print("the first non repeating charater is",s)
# #     else:
# #         ("all are repeating characters")



# students = ["Ravi", "Anil", "Kiran", "Suresh"]
# for student in students:
#     if student == "Kiran":
#         print("student found :",student)
#         break
#     else:
#         print("student not found")


# students = ["Ravi", "Anil", "Kiran", "Suresh"]
# for i in range(len(students)):
#     if students[i] == "Kiran":
#         print("Student found:", students[i])
#     else:
#         print("Student not found") 






my_str = input("Enter a string: ") #Nagababu

freq = {}

for char in my_str:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

for char in my_str:
    if freq[char] == 1:
        print("non-repe char:", char)
        break




# my_str = input("Enter a string: ")

# freq = {}

# for char in my_str:
#     if char in freq:
#         freq[char] = freq[char] + 1
#     else:
#         freq[char] = 1

# count = 0  

# for char in my_str:
#     if freq[char] == 1:
#         count = count + 1
#         if count == 3:
#             print("2nd non-rep char:", char)
#             break


