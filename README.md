#GenAI_Assignment5: Importing_creating_modules-packages
This assignment focuses on understanding Python modules and packages in a simple and beginner-friendly way.
Topics Covered:
Creating Python modules (.py files)
Importing modules
Creating packages using __init__.py
Using different import methods
folder Structure 
modules_assignment/
│
├── main.ipynb
├── math_utils.py
├── string_utils.py
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
    
Task 1: math_utils Module
File: math_utils.py
Functions:
add(a, b) → returns sum
subtract(a, b) → returns difference
square(n) → returns square of number
Example:
import math_utils
from math_utils import square
print(math_utils.add(10, 5))     # 15
print(math_utils.subtract(8, 6)) # 2
print(square(8))                 # 64

Task 2: string_utils Module
File: string_utils.py
Functions:
capitalize_words(text) → capitalizes each word
reverse_string(text) → reverses string
word_count(text) → counts words
Example:
Python
import string_utils
text = "hello world from python"
print(string_utils.capitalize_words(text))
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))

Task 3: shop_package (Package)
A package named shop_package is created containing:
File:discount.py
Functions:
apply_discount(price, percent) → returns discounted price
flat_discount(price) → subtracts 50
File: billing.py
Functions:
calculate_total(prices) → sum of prices
apply_tax(amount) → adds 5% tax
File: __init__.py
Python
from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax

Task 4: Using Package in main.py
Imports used:
Python
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax
Example:
Python
print(disc.apply_discount(1000, 10))  # 900.0
print(disc.flat_discount(1000))       # 950
print(calculate_total([100, 200, 300])) # 600
print(apply_tax(600))                 # 630.0

Run main.ipyb file in Jupiter notebook 
or copy the code and create main.py file and run in vs code.
