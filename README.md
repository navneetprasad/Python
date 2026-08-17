# Python Fundamentals & String Manipulation

A consolidated reference guide covering Python basics, data types, functions, escape sequences, and string operations[cite: 1, 2].

---

## 1. Variables & Data Types

Variables dynamically store and update values.

```python
# Variables & Calculations
name = "Jaskirat Singh"
name = "Ajit Doval"  # Reassignment

a = 10
b = 20
c = a + b  # 30

2. I/O & Functions vs. Methods
import math[cite: 1]

# Built-in & Custom Functions
print("Sum:", 10 + 20)  # Multiple arguments[cite: 1]
user_name = input("Enter your name: ")[cite: 1]
print(len("Jaskirat Singh"))      # Output: 14[cite: 1]
print(math.sqrt(16))              # Output: 4.0[cite: 1]

def greet(name):[cite: 1]
    return "Hello, " + name + "!"[cite: 1]

# Functions vs. Methods
text = "Hello, World!"[cite: 1]
num = 10[cite: 1]

print(type(text))          # Function -> <class 'str'>[cite: 1]
print(text.upper())        # String Method -> HELLO, WORLD![cite: 1]
print(num.bit_length())    # Integer Method -> 4[cite: 1]

3. Escape Sequences
print("Line 1\nLine 2")                                      # \n  : New line[cite: 2]
print("Hi\tEveryone")                                        # \t  : Tab space[cite: 2]
print("C:\\Users\\Navneet Prasad\\OneDrive\\Documents")      # \\  : Literal backslash[cite: 2]
print("She said, \"Hello!\"")                               # \"  : Escaped double quotes[cite: 2]

4. String Manipulation Reference
# f-Strings & .format()
name, lang = "Jaskirat Singh", "Python"[cite: 2]
print(f"My name is {name} and I am learning {lang}")[cite: 2]
print("Hi {n}, order {o}".format(n="Jaskirat", o=1))[cite: 2]

# Replace, Split & Join
date = "14.08.2026"[cite: 2]
print(date.replace(".", "-"))  # Output: 14-08-2026[cite: 2]

csv_data = "Navneet,25,Delhi"[cite: 2]
name, age, city = csv_data.split(",")[cite: 2]

parts = ["2026", "08", "14"][cite: 2]
print("-".join(parts))         # Output: 2026-08-14[cite: 2]

Indexing & Slicing
code = "Jaskirat Singh-Python Developer"[cite: 2]

print(code[0])       # Output: J (First char)[cite: 2]
print(code[-1])      # Output: r (Last char)[cite: 2]
print(code[0:8])     # Output: Jaskirat (Slice range)[cite: 2]

Trimming & Searching
# Trimming Whitespace & Characters
name = "  Jaskirat  "[cite: 2]
print(name.strip())                # Output: Jaskirat[cite: 2]
print("$Jaskirat$".strip("$"))      # Output: Jaskirat[cite: 2]

# Case-Insensitive Comparison
search, data = "EMAIL", "email"[cite: 2]
print(search.lower().strip() == data.lower().strip())  # Output: True[cite: 2]

# Prefix / Suffix / Substring Search
phone = "123-456-7890"[cite: 2]
print(phone.startswith("123"))     # Output: True[cite: 2]
print("document.pdf".endswith(".pdf")) # Output: True[cite: 2]
print("@" in "user@example.com")   # Output: True[cite: 2]

# Dynamic Slicing via .find()
print(phone[phone.find("-") + 1:]) # Output: 456-7890[cite: 2]

Validation & Padding
# Validation
print("USA".isalpha())     # Output: True[cite: 2]
print("123".isnumeric())   # Output: True[cite: 2]

# Zero-Padding
print("42".zfill(5))       # Output: 00042[cite: 2]
