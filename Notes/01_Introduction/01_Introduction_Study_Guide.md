Here is the complete study guide formatted as a single, clean Markdown file. You can click the "Copy" button on the top right of the code block and paste it directly into a new file named `Introduction_Study_Guide.md` inside your `01_Introduction` folder.

```markdown
# Chapter 1: Introduction to Python - Complete Study Guide

## Table of Contents
- [1. Numbers and Arithmetic](#1-numbers-and-arithmetic)
- [2. Strings and Text](#2-strings-and-text)
- [3. Lists and Data Structures](#3-lists-and-data-structures)
- [4. File Management](#4-file-management)
- [5. Functions and Error Handling](#5-functions-and-error-handling)
- [Practical Projects](#practical-projects)
- [Key Concepts & Best Practices](#key-concepts--best-practices)

---

## 1. Numbers and Arithmetic

### Number Types
```python
# Integers (whole numbers)
age = 30
shares = 100

# Floating-point (decimals)
price = 32.20
interest_rate = 0.05

# Check type
type(42)      # <class 'int'>
type(3.14)    # <class 'float'>
```

### Arithmetic Operations
```python
x = 10 + 5   # Addition: 15
y = 10 - 5   # Subtraction: 5
z = 10 * 5   # Multiplication: 50
w = 10 / 3   # Division: 3.333...
q = 10 // 3  # Floor division: 3
r = 10 % 3   # Modulus (remainder): 1
p = 10 ** 2  # Exponentiation: 100
```

### Type Conversion
```python
int("100")        # String to integer: 100
float("32.20")    # String to float: 32.20
str(42)           # Integer to string: "42"
```

---

## 2. Strings and Text

### Creating and Manipulating Strings
```python
name = "Alice"
greeting = 'Hello'

# Concatenation
full_name = "Alice" + " " + "Smith"  

# Length
len("Hello")  # 5
```

### String Methods
```python
text = "  Hello World  "

text.upper()          # "  HELLO WORLD  "
text.lower()          # "  hello world  "
text.strip()          # "Hello World" (remove whitespace)
text.replace("World", "Python")  # "  Hello Python  "
text.split()          # ['Hello', 'World']
text.find("World")    # 7 (position)
```

### String Indexing and Slicing
```python
name = "Python"

name[0]      # 'P' (first character)
name[-1]     # 'n' (last character)
name[0:3]    # 'Pyt' (slice from 0 to 3)
name[:3]     # 'Pyt' (same as above)
name[3:]     # 'hon' (from index 3 to end)
```

### f-Strings (Formatted Strings)
```python
name = "Alice"
price = 44671.15

f"Hello, {name}!"                    # "Hello, Alice!"
f"Total cost: ${price:.2f}"          # "Total cost: $44671.15"
```

---

## 3. Lists and Data Structures

### Creating and Accessing Lists
```python
# Empty list
empty = []

# List with items
stocks = ["AAPL", "IBM", "MSFT", "GOOG"]

# Accessing elements
stocks[0]      # "AAPL" (first item)
stocks[-1]     # "GOOG" (last item)
stocks[1:3]    # ["IBM", "MSFT"] (slice)
```

### Modifying Lists
```python
stocks = ["AAPL", "IBM", "MSFT"]

stocks.append("GOOG")           # Add to end
stocks.insert(1, "TSLA")        # Insert at position
stocks.remove("IBM")            # Remove by value
last = stocks.pop()             # Remove and return last item
del stocks[0]                   # Delete by index
stocks[0] = "AMZN"              # Change value
```

### List Operations & Methods
```python
len(stocks)                     # Length: 4
"AAPL" in stocks                # Membership: True
stocks.extend(["TSLA", "META"]) # Add multiple items
stocks.index("IBM")             # Find position: 1
stocks.sort()                   # Sort alphabetically
```

### Nested Lists
```python
portfolio = [
    ["AAPL", 100, 32.20],
    ["IBM", 50, 91.10]
]

portfolio[0]        # ["AAPL", 100, 32.20]
portfolio[0][0]     # "AAPL"
```

---

## 4. File Management

### Opening Files (Best Practice)
Always use the `with` statement. It automatically closes the file when the block finishes, even if an error occurs.
```python
with open('portfolio.csv', 'rt') as file:
    data = file.read()
# File is automatically closed here
```

### File Modes
- `'r'` or `'rt'`: Read text (default)
- `'w'` or `'wt'`: Write text (overwrites)
- `'a'` or `'at'`: Append text

### Reading Files
```python
# Read entire file as a single string
with open('data.txt', 'rt') as f:
    data = f.read()

# Read line by line (Memory efficient!)
with open('data.txt', 'rt') as f:
    for line in f:
        print(line, end='')
```

### Writing to Files
```python
with open('output.txt', 'wt') as f:
    f.write("Hello World\n")

# Or redirect print to file
with open('output.txt', 'wt') as f:
    print("Hello World", file=f)
```

### Working with CSV Files
**Manual Parsing:**
```python
with open('portfolio.csv', 'rt') as f:
    for line in f:
        clean_line = line.strip()
        columns = clean_line.split(',')
        name = columns[0]
```

**Using the `csv` Module (Recommended):**
```python
import csv

with open('portfolio.csv', 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header row automatically
    
    for row in rows:
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
```

### Reading Compressed Files
```python
import gzip

with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
```

---

## 5. Functions and Error Handling

### Defining Functions
```python
def greet(name):
    """Say hello to someone (Docstring)"""
    return f"Hello, {name}!"

message = greet("Alice")
```

### Error Handling (Try-Except)
Use this to prevent your program from crashing when it encounters bad data.
```python
try:
    shares = int("100")
    price = float("abc")  # This will cause a ValueError
except ValueError:
    print("Could not convert to number")
except IndexError:
    print("Index out of range")
```

### Raising Exceptions
You can manually trigger an error if your code encounters an invalid state.
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

### Command-Line Arguments
Make your scripts flexible by accepting arguments from the terminal.
```python
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f"Processing {filename}...")
```
*Run from terminal:* `python3 script.py Data/portfolio.csv`

---

## Practical Projects

### Project 1: Portfolio Cost Calculator
```python
import csv

def portfolio_cost(filename):
    """Calculate total cost of portfolio from a CSV file."""
    total_cost = 0.0
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except (ValueError, IndexError):
                pass  # Skip header row and bad data
    
    return total_cost

# Test it
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 pcost.py <filename>")
        sys.exit(1)
        
    cost = portfolio_cost(sys.argv[1])
    print(f"Total cost: ${cost:.2f}")
```

---

## Key Concepts & Best Practices

### Essential Skills
1. **Reading files:** Always use the `with open()` pattern.
2. **Parsing data:** Use `.strip()` and `.split()` for manual parsing, or the `csv` module for robust parsing.
3. **Error handling:** Use `try-except` blocks when dealing with external data or user input.
4. **Writing functions:** Wrap reusable logic in functions with clear parameters and return values.

### Best Practices Checklist
- ✅ Use `with` for file operations (auto-closes files).
- ✅ Handle errors gracefully; don't let bad data crash the whole program.
- ✅ Write functions for reusability.
- ✅ Use meaningful variable names (`total_cost` instead of `x`).
- ✅ Add comments and docstrings to explain *why* code does something.
- ✅ Use f-strings for clean text formatting.
- ✅ Process files line-by-line for large datasets to save memory.

---
**End of Chapter 1 Study Guide**
```