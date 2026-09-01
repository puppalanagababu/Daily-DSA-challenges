#1. CODING PROBLEM — STUDENT MARKS ANALYZER

students = {
    "Ravi": 85,
    "Anil": 72,
    "Kiran": 91,
    "Suresh": 68,
    "Priya": 91
}

highest = 0
total = 0
above_80 = []
passed = 0

for name, marks in students.items():
    if marks > highest:         # Highest marks
        highest = marks

    total += marks  # Total marks

    if marks > 80:      # Above 80
        above_80.append(name)
    
    if marks >= 40:         # Passed
        passed += 1

average = total / len(students)

print("Highest Marks:", highest)
print("Average Marks:", average)
print("Students Above 80:", above_80)
print("Number of Students Passed:", passed)

# 3. DEBUGGING CHALLENGE — MUTABLE DEFAULT ARGUMENT
'''
10. Actual Output

["Ravi"]
["Ravi", "Anil"]
["Ravi", "Anil", "Kiran"]

11. Why does this happen?

The problem is:

students=[]

A mutable default argument is created only once, when the function is defined.

So every function call uses the same list.

1st call → ["Ravi"]

2nd call → same list → ["Ravi", "Anil"]

3rd call → same list → ["Ravi", "Anil", "Kiran"]
'''

#12. Fix the function

#Use `None` as the default value:

def add_student(name, students=None):
    if students is None:
        students = []

    students.append(name)
    return students


print(add_student("Ravi"))
print(add_student("Anil"))
print(add_student("Kiran"))

#  Output
# ["Ravi"]
# ["Anil"]
# ["Kiran"]


'''
13. explain 
"The problem is using a list as a default argument. Python creates that list only once, so all function calls share the same list. To avoid this, we use `None` as the default value and create a new list inside the function."

def function(data=[]):      # Avoid

def function(data=None):    # Correct
    if data is None:
        data = []

'''

# 4. MINI CHALLENGE — REMOVE DUPLICATES

#A. Using a Set

def remove_duplicates(numbers):
    result = []
    seen = set()

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


print(remove_duplicates([10, 20, 10, 30, 20, 40, 30]))
print(remove_duplicates([3, 1, 3, 2, 1, 5]))

#Output

[10, 20, 30, 40]
[3, 1, 2, 5]

#Logic
'''
Take each number
      ↓
Check if already seen
      ↓
No → Add to result + set
Yes → Skip
'''

#B. Without Using a Set

def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result


print(remove_duplicates([10, 20, 10, 30, 20, 40, 30]))
print(remove_duplicates([3, 1, 3, 2, 1, 5]))

#Output

[10, 20, 30, 40]
[3, 1, 2, 5]

#Logic
'''
For every number, check whether it is already in `result`.

10 → not there → add
20 → not there → add
10 → already there → skip
30 → not there → add
20 → already there → skip
'''

#1st code

'''1. Highest marks
Start highest = 0
Check every student's marks
If marks > highest:
    update highest
2. Average
Add all marks
Divide total by number of students
3. Above 80
text
Check every student
If marks > 80:
    add student name
4. Passed
text
Check every student
If marks >= 40:
    increase passed count
'''


# 2. CONCEPT QUESTION — LIST VS DICTIONARY
    
'''
 6. Difference between List and Dictionary

List
students = [
    ["Ravi", 85],
    ["Anil", 72],
    ["Kiran", 91]
]
* Stores data in order.
* We access data using an **index**.
* Searching by name requires checking each element.

Dictionary
students = {
    "Ravi": 85,
    "Anil": 72,
    "Kiran": 91
}
* Stores data as **key-value pairs**.
* Student name is the **key** and marks are the **value**.
* We can directly search using the name.

7. Which one is better for searching marks by name?

Dictionary is better.

print(students["Kiran"])

Output:
91

Because we can directly use the student name as a key.

8. Average time complexity of dictionary lookup

**O(1)** in typical cases.

Example:

students["Kiran"]

It usually finds the value directly.

9. When is a list better?

A list is better when we mainly need to maintain data in order or process every item.

Example:
marks = [85, 72, 91, 68, 75]

If we want to **sort marks, loop through all marks, or access them by position**, a list is a good choice.

Easy way to remember

List       → Access by index → students[0]
Dictionary → Access by key   → students["Ravi"]

Dictionary lookup → O(1)

'''