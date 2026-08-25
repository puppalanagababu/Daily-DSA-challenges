# # without Encapsulation :


# class Bank:
# 	def __init__(self):
# 		self.balance = 1000

# 	def show_balance(self):
# 		print(self.balance)
	
# 	def deposit(self, amount):
# 		self.balance += amount
	

# b = Bank()

# b.deposit(2000)
# b.show_balance()


# class Student:
#     def __init__(age, name, fullname):
#         age.name=name
#         age.fullname=fullname
#         return(age.name + age.fullname)
# s1=Student("babu", "nagababu")
# print(s1)
    

# class Student:

#     def __init__(xyz, name, fullname):
#         xyz.name = name
#         xyz.fullname = fullname

#     def display(xyz):
#         print( xyz.name + xyz.fullname)

# s1 = Student("Babu", "Naidu")
# print(s1.display())


# class Student:
#     def display(xyz):
#         return xyz.name + " " + xyz.fullname

#     def __init__(xyz, name, fullname):
#         xyz.name = name
#         xyz.fullname = fullname
#         xyz.display()

# s1 = Student("Babu", "Naidu")
# print(s1.display())

class Student:
    def display(xyz):
        return xyz.name + " " + xyz.fullname

    def __init__(xyz, name, fullname):
        xyz.name = name
        xyz.fullname = fullname
        # print(xyz.display())
print(Student.display())
print(Student("Babu", "Naidu").display())
# s1 = Student()