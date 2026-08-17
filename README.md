# Python Basics & Fundamentals Reference Guide

A comprehensive quick-reference guide and documentation covering fundamental Python concepts, data types, string operations, arithmetic/logical operations, built-in functions, and list manipulations based on core starter scripts.

---

## 📋 Table of Contents

- [1. Variables & Printing](#1-variables--printing)
  - [Variable Assignment & Reassignment](#variable-assignment--reassignment)
  - [Formatted Strings (f-strings) & Output](#formatted-strings-f-strings--output)
  - [Escape Sequences](#escape-sequences)
- [2. Data Types](#2-data-types)
  - [Primitive & Core Types](#primitive--core-types)
  - [Type Inspection](#type-inspection)
- [3. String Operations & Methods](#3-string-operations--methods)
  - [Indexing & Slicing](#indexing--slicing)
  - [String Transformation & Cleaning](#string-transformation--cleaning)
  - [Searching & Inspection](#searching--inspection)
  - [Validation, Formatting & Joining](#validation-formatting--joining)
- [4. Numbers, Arithmetic & Math](#4-numbers-arithmetic--math)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Comparison & Logical Operators](#comparison--logical-operators)
  - [Math Module & Rounding Functions](#math-module--rounding-functions)
- [5. Lists & Collections](#5-lists--collections)
  - [Creating Lists](#creating-lists)
  - [List Methods & Operations](#list-methods--operations)
- [6. Functions vs Methods](#6-functions-vs-methods)
  - [Built-in Functions](#built-in-functions)
  - [Class Methods](#class-methods)
  - [User-Defined Functions](#user-defined-functions)

---

## 1. Variables & Printing

### Variable Assignment & Reassignment
Variables in Python are dynamically typed and can be assigned or updated directly without explicit type declaration.

```python
# Initial assignment
name = "Jaskirat Singh"
age = 25
language = "Python"

# Reassigning variables
name = "Ajit Doval"
```

### Formatted Strings (f-strings) & Output
f-strings provide an intuitive and concise way to embed expressions inside string literals.

```python
name = "Jaskirat Singh"
language = "Python"

print(f"My name is {name}")
print(f"I am learning {language}")
```

### Escape Sequences
Escape characters allow inserting special characters into strings:

| Sequence | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `\n` | Newline | `print("Line 1\nLine 2")` | Line 1<br>Line 2 |
| `\t` | Tab space | `print("Hi\tEveryone")` | Hi    Everyone |
| `\\` | Backslash | `print("C:\\Users\\Documents")` | C:\Users\Documents |
| `\"` | Double quote | `print("She said, \"Hello!\"")` | She said, "Hello!" |

---

## 2. Data Types

### Primitive & Core Types

```python
# Text
name = "Jaskirat Singh"       # str

# Numeric
age = 25                      # int
height = 5.9                  # float
complex_num = 2 + 3j          # complex

# Boolean
is_student = True             # bool (True / False)

# None Type
empty_val = None              # NoneType

# Sequences & Collections
numbers = [1, 2, 3, 4, 5]     # list
coordinates = (1, 2)          # tuple
```

### Type Inspection

```python
x = 10
y = 3.14
z = 2 + 3j

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```

---

## 3. String Operations & Methods

### Indexing & Slicing
Strings are zero-indexed and support both forward and negative indexing as well as slicing (`[start:stop:step]`).

```python
code = "Jaskirat Singh-Python Developer"

# Accessing single characters
print(code[0])    # 'J' (First character)
print(code[-1])   # 'r' (Last character)

# Slicing substring [start:end]
print(code[0:8])  # 'Jaskirat'

# Slicing date strings
date = "14.08.2026"
print(date[0:2])  # '14' (Day)
print(date[3:5])  # '08' (Month)
print(date[6:])   # '2026' (Year)
```

### String Transformation & Cleaning

```python
# Replace characters
date = "14.08.2026"
print(date.replace(".", "-"))  # '14-08-2026'

# Splitting CSV formatted data
csv_data = "Navneet,25,Delhi"
name, age, city = csv_data.split(",")
print(f"Name: {name}, Age: {age}, City: {city}")

# Stripping whitespace & specific characters
text = "  Jaskirat  "
print(text.strip())            # 'Jaskirat'
print(text.lstrip())           # 'Jaskirat  '
print(text.rstrip())           # '  Jaskirat'
print("$Jaskirat$".strip("$")) # 'Jaskirat'

# Case-insensitive comparison
search = "EMAIL"
data = "email"
print(search.lower().strip() == data.lower().strip())  # True
```

### Searching & Inspection

```python
phone = "123-456-7890"
email = "user@example.com"
file_name = "document.pdf"

# Prefix / Suffix checks
print(phone.startswith("123"))   # True
print(file_name.endswith(".pdf")) # True

# Finding substring positions & existence
print(email.find("@") != -1)     # True
print("@" in email)              # True

# Dynamic slicing with find()
first_hyphen = phone.find("-")
print(phone[first_hyphen + 1:])  # '456-7890'
```

### Validation, Formatting & Joining

```python
# Validation
print("USA".isalpha())     # True (contains only alphabets)
print("123".isnumeric())   # True (contains only numbers)

# Joining sequences
parts = ["2026", "08", "14"]
print("-".join(parts))     # '2026-08-14'

# str.format()
print("Hi {n}, order {o}".format(n="Jaskirat", o=1)) # 'Hi Jaskirat, order 1'

# Zero-padding numbers (zfill)
print("42".zfill(5))       # '00042'
```

---

## 4. Numbers, Arithmetic & Math

### Arithmetic Operators

| Operator | Description | Example (`a = 10, b = 3`) | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | Division (Float) | `a / b` | `3.3333...` |
| `//` | Floor Division | `a // b` | `3` |
| `%` | Modulus (Remainder) | `a % b` | `1` |
| `**` | Exponentiation | `a ** b` | `1000` |

### Comparison & Logical Operators

```python
x = 10
y = 20

# Comparisons
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x >= y)  # False

# Logical Operators (and, or, not)
print(x < 15 and y > 15)  # True
print(x < 15 or y < 15)   # True
print(not(x == y))         # True
```

### Math Module & Rounding Functions

```python
import math

# Ceil (rounds up)
print(math.ceil(4.2))   # 5
print(math.ceil(4.8))   # 5

# Floor (rounds down)
print(math.floor(4.2))  # 4
print(math.floor(4.8))  # 4

# Round (standard rounding)
print(round(4.2))       # 4
print(round(4.8))       # 5

# Square root
print(math.sqrt(16))    # 4.0
```

---

## 5. Lists & Collections

### Creating Lists

```python
# Homogeneous lists
numbers = [1, 2, 3, 4, 5]
names = ["Jaskirat", "Singh", "Python"]
flags = [True, False, True]

# Heterogeneous (mixed) list
mixed_list = [1, "Jaskirat", True, 3.14]

# Access by index
print(mixed_list[1])  # 'Jaskirat'
```

### List Methods & Operations

```python
names = ["Jaskirat", "Singh", "Python"]

# Add element to end
names.append("Developer")
# ['Jaskirat', 'Singh', 'Python', 'Developer']

# Remove specific value
names.remove("Singh")
# ['Jaskirat', 'Python', 'Developer']

# Remove by index with pop()
removed_item = names.pop(1)  # Removes 'Python'
# names: ['Jaskirat', 'Developer']

# Membership test
print("Jaskirat" in names)   # True
print("Singh" in names)      # False

# Length of list
print(len(names))            # 2

# Sorting and reversing
names.append("Rehman Dakkait")
names.append("Modi")

names.sort()     # Alphabetical order: ['Developer', 'Jaskirat', 'Modi', 'Rehman Dakkait']
names.reverse()  # Reverse order: ['Rehman Dakkait', 'Modi', 'Jaskirat', 'Developer']
```

---

## 6. Functions vs Methods

### Built-in Functions
Functions are standalone blocks of code called independently on inputs.

```python
text = "Hello, World!"

print(len(text))    # 13
print(type(text))   # <class 'str'>

# Taking user input
# user_name = input("Enter your name: ")
```

### Class Methods
Methods are functions bound to a specific class instance and invoked via the dot operator (`object.method()`).

```python
text = "Hello, World!"
num = 10

# String method
print(text.upper())       # 'HELLO, WORLD!'

# Integer method
print(num.bit_length())   # 4
```

### User-Defined Functions
Defined using the `def` keyword.

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

message = greet("Jaskirat Singh")
print(message)  # "Hello, Jaskirat Singh!"
```

---

## 🚀 Getting Started

1. Ensure Python 3.8+ is installed on your system.
2. Run any example interactively using the Python REPL:
   ```bash
   python -i
   ```
3. Or save snippets to a script (e.g., `main.py`) and run:
   ```bash
   python main.py
   ```
