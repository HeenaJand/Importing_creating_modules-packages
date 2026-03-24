##Checking path of files and folders exists correctly or not
import os
print("Current Folder")
print(os.getcwd())

print("\n Files in current folder:")
print(os.listdir())

print("\n Does modules_assignment exists?")
print(os.path.exists("modules_assignment"))

if os.path.exists("modules_assignment"):
    print("\n Files inside modules_assignment:")
    print(os.listdir("modules_assignment"))

import sys
sys.path.append("modules_assignment")

#Task 1 Testing
import math_utils
from math_utils import square 


print(math_utils.add(10,5))
print(math_utils.subtract(8,6))
print(square(8))

#Task 2 Testing 
import string_utils
text= "hello world, this is to test string_utils module"

print(string_utils.capitalize_words(text))
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))

#Task 3 & 4 Testing 
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax

print(disc.apply_discount(1000,10))
print(disc.flat_discount(1000))
print(calculate_total([100,130,200]))
print(apply_tax(600))











