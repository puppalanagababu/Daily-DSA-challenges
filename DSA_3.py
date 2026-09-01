# 1. CODING PROBLEM — CHARACTER FREQUENCY

def character_frequency(text):
    freq = {}
    for char in text:
        if char == " ":
            continue  # Ignore spaces
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# 2. CONCEPT QUESTION — FUNCTIONS
"""
1. What is a function?
   A function is a reusable block of organized code that performs a specific task.
   It only runs when it is called and can take inputs and return outputs.

2. Why do we use functions?
   - Reusability: Write code once and use it many times (DRY principle: Don't Repeat Yourself).
   - Modularity: Breaks complex problems into smaller, manageable chunks.
   - Readability & Maintainability: Easier to understand, test, and fix bugs.

3. Difference between a Parameter and an Argument:
   - Parameter: The variable listed inside the parentheses in the function DEFINITION (e.g., `name` in `def greet(name):`).
   - Argument: The actual value passed to the function when it is CALLED (e.g., `"Ravi"` in `greet("Ravi")`).

Example Identification:
    def greet(name):
        print("Hello", name)
    greet("Ravi")

    - Function name: greet
    - Parameter: name
    - Argument: "Ravi"

Return vs Print:
    def add(a, b):
        print(a + b)
    - Just displays the result on the screen/console. It returns `None` to the caller.
    - We CANNOT store or use the result in further calculations.

    def add(a, b):
        return a + b
    - Sends the result back to the caller so it can be stored in a variable or used in further operations.

Interview Follow-up:
    def test():
        x = 10
    result = test()
    print(result)

    Output: None
    Why: The function `test()` defines a local variable `x = 10`, but it does not have a `return` statement.
         In Python, functions without an explicit return statement automatically return `None`.
"""


# 3. DEBUGGING CHALLENGE — Return vs Print
"""
What was the problem?
The student's function `calculate_total` printed `total` instead of returning it.
Therefore, `result = calculate_total(100, 3)` assigned `None` to `result`.
When computing `result * 0.10`, Python raises a `TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'`.

Why did it happen?
`print()` only writes to the console; it doesn't give a value back to the caller.

My Corrected Code:
"""

def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(100, 3)
discount = result * 0.10

print("--- 3. Debugging Challenge ---")
print("Total:", result)
print("Discount:", discount)


# 4. MINI PROBLEM — PASSWORD VALIDATOR
"""
My Approach:
1. Check if the length of `password` is at least 8. If not, return "Invalid Password".
2. Initialize boolean flags: `has_upper = False`, `has_lower = False`, `has_digit = False`, `has_special = False`.
3. Define special characters: `!@#$%^&*()-_+=<>?/`
4. Loop through each character in `password`:
   - if `char.isupper()`, set `has_upper = True`
   - elif `char.islower()`, set `has_lower = True`
   - elif `char.isdigit()`, set `has_digit = True`
   - elif `char in special_chars`, set `has_special = True`
5. If all required conditions are True, return "Valid Password", otherwise return "Invalid Password".
"""

def validate_password(password, check_special=False):
    if len(password) < 8:
        return "Invalid Password"
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_+=<>?/{}[]~`"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if check_special:
        if has_upper and has_lower and has_digit and has_special:
            return "Valid Password"
    else:
        if has_upper and has_lower and has_digit:
            return "Valid Password"
            
    return "Invalid Password"


print("--- 4. Password Validator Test Cases ---")
print("Test Case 1 ('Hello123'):", validate_password("Hello123"))          # Valid
print("Test Case 2 ('hello'):", validate_password("hello"))                # Invalid (too short, no upper, no digit)
print("Test Case 3 ('Password'):", validate_password("Password"))          # Invalid (no digit)
print("Bonus Test ('SecurePass123!'):", validate_password("SecurePass123!", check_special=True))  # Valid
print("Bonus Test ('SecurePass123'):", validate_password("SecurePass123", check_special=True))    # Invalid (no special char)
print()


# 5. MINI INTERVIEW ROUND
"""
Q1: What happens when a Python function does not have a return statement?
    Ans: It returns `None` by default when the execution reaches the end of the function block.

Q2: Can a function return multiple values?
    Ans: Yes! In Python, separating values with commas (e.g. `return a, b`) returns them packed as a tuple.
         Example:
         def get_dimensions():
             return 1920, 1080
         w, h = get_dimensions()

Q3: What is the difference between a local variable and a global variable?
    Ans:
    - Local variable: Defined inside a function. It is only accessible within that function and destroyed after execution.
    - Global variable: Defined outside of any function (at module level). It is accessible throughout the entire file.

Q4: What does def calculate(a, b=10): mean? What is b=10?
    Ans: `b=10` is a default parameter. If the caller provides an argument for `b`, that value is used;
         if the caller omits `b`, it defaults to 10.
         Example: `calculate(5)` uses `a=5, b=10`. `calculate(5, 20)` uses `a=5, b=20`.

Q5: What is the purpose of if __name__ == '__main__':?
    Ans: It checks whether the Python script is being run directly by the user or imported as a module in another script.
         Code inside this block only executes when the file is run directly, preventing unintended code execution upon import.
"""
