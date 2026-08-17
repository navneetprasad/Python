# #Without Variables
# print("My name is Jaskirat Singh")
# print("I am 25 years old")

# #With Variables
# name = "Jaskirat Singh"
# language = "Python"
# print(f"My name is {name}")
# print(f"I am learning {language}")

#Escape Sequences
# print("Line 1\nLine 2") #Output: Line 1
# print("Hi\tEveryone") #Output: Hi    Everyone
# print("C:\\Users\\Navneet Prasad\\OneDrive\\Documents\\WB Games")
# print("She said, \"Hello!\"") #Output: She said, "Hello!"

#String Transformations
# date = "14.08.2026"
# print(date.replace(".", "-")) #Output: 14-08-2026

# first_name = "Jaskirat"
# last_name = "Singh"
# full_name = f"{first_name} {last_name}"
# print(full_name) #Output: Jaskirat Singh

# csv_data = "Navneet,25,Delhi"
# name, age, city = csv_data.split(",")
# print(f"Name: {name}, Age: {age}, City: {city}")

# print("============")

# code = "Jaskirat Singh-Python Developer"
# print(code[0]) #Output: J
# print(code[-1]) #Output: r
# print(code[0:8]) #Output: Jaskirat

# date = "14.08.2026"
# print((date[0:2])) #Output: 14
# print((date[3:5])) #Output: 08
# print((date[-2])) #Output: 2026

# print(code[0:9]) #Output: Jaskirat Singh

#String Slicing
# name = "Jaskirat"
# print(name.strip()) #Output: Jaskirat
# print(name.lstrip()) #Output: jaskirat
# print(name.rstrip()) #Output: Jaskirat

# #strip specific characters
# print("$Jaskirat$".strip("$")) #Output: Jaskirat

# #case-insensitive comparison
# search = "EMAIL"
# data = "email"
# print(search.lower().strip() == data.lower().strip()) #Output: True

# #String Searching
# phone = "123-456-7890"
# print(phone.startswith("123")) #Output: True

# file = "document.pdf"
# print(file.endswith(".pdf")) #Output: True

# email = "user@example.com"
# print(email.find("@") != -1) #Output: True
# print(("@" in email)) #Output: True

# #use find() to slice dynamically
# print(phone[phone.find("-")+1:]) #Output: 456-7890

# Strings Validate,Join,Format

#Validation
# print("USA".isalpha()) #Output: True
# print("123".isnumeric()) #Output: True

# #join
# parts = ["2026", "08", "14"]
# print("-".join(parts)) #Output: 2026-08-14

# #format
# print("Hi {n}, order {o}".format(n="Jaskirat", o=1)) #Output: Hi Jaskirat, order 1

# #zfill
# print("42".zfill(5)) #Output: 00042

#Numeric data types
# x = 10 #Integer
# y = 3.14 #Float
# z = 2 + 3j #Complex

# print(type(x)) #Output: <class 'int'>
# print(type(y)) #Output: <class 'float'>
# print(type(z)) #Output: <class 'complex'>

# #Arithmetic Operations
# a = 10
# b = 3

# print(a + b) #Output: 13
# print(a - b) #Output: 7
# print(a * b) #Output: 30
# print(a / b) #Output: 3.3333333333333335 #float
# print(a // b) #Output: 3 #floor
# print(a % b) #Output: 1 #modulus
# print(a ** b) #Output: 1000 #power

#Comparison Operators
# x = 10
# y = 20
# print(x == y) #Output: False
# print(x != y) #Output: True
# print(x < y) #Output: True
# print(x > y) #Output: False
# print(x <= y) #Output: True
# print(x >= y) #Output: False

# #Logical Operators
# print(x < 15 and y > 15) #Output: True
# print(x < 15 or y < 15) #Output: True
# print(not(x == y)) #Output: True

#Rounding Modules
# import math
# x = 10
# y = 3

# #Ceil
# print(math.ceil(4.2)) #Output: 5
# print(math.ceil(4.8)) #Output: 5
# #Floor
# print(math.floor(4.2)) #Output: 4
# print(math.floor(4.8)) #Output: 4
# #Round
# print(round(4.2)) #Output: 4
# print(round(4.8)) #Output: 5

# #Numbers
# numbers = [1, 2, 3, 4, 5]
# #String
# names = ["Jaskirat", "Singh", "Python"]
# #Boolean
# flags = [True, False, True]
# #Mixed 
# mixed_list = [1, "Jaskirat", True, 3.14]
# print(numbers) #Output: [1, 2, 3, 4, 5]
# print(names) #Output: ['Jaskirat', 'Singh', 'Python']
# print(flags) #Output: [True, False, True]

# print(mixed_list[1]) #Output: Jaskirat

#List Operations
# names = ["Jaskirat", "Singh", "Python"]
# print("Original List:", names) #Output: Original List: ['Jaskirat', 'Singh', 'Python']
# names.append("Developer")
# print("After append('Developer'):", names) #Output: After Append: ['Jaskirat',
# names.remove("Singh")
# print("After remove('Singh'):", names) #Output: After Remove: ['Jaskirat', 'Python', 'Developer']
# removed_name = names.pop(1)
# print("Removed using pop(1):", removed_name) #Output: Removed using pop(1): Python
# print("List after pop():", names) #Output: List after pop(1): ['Jaskirat', 'Developer']
# print("Length of List:", len(names)) #Output: Length of List: 2

# #names is now ['Jaskirat', 'Developer']
# print("Is 'Jaskirat' in names?", "Jaskirat" in names) #Output: Is 'Jaskirat' in names? True
# print("Is 'Singh' in names?", "Singh" in names) #Output: Is 'Singh' in names? False
# names.append("Rehamn Dakkait")
# names.append("Modi")
# print("Before Sorting:", names) #Output: Before Sorting: ['Jaskirat', 'Developer', 'Rehamn Dakkait', 'Modi']
# names.sort()    #sort alphabetically
# print("After Sorting:", names) #Output: After Sorting: ['Developer', 'Jaskirat', 'Modi', 'Rehamn Dakkait']
# names.reverse() #reverse the list
