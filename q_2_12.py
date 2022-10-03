"""
Python Programming in Context
"""

# This module is used to compare your implementation of factorial to a correct
# one.
import math


#################################### 2.12 ######################################
# Write a function called factorial that computes the product of the first n
# numbers, starting at 1, including n.
# Use a for loop and an accumulator variable.

def factorial(n):
    # REPLACE THIS CODE:
    pass

# This code will compare your answers to the correct ones:
print(f"{factorial(1)=}  <-- this should be {math.factorial(1)}")
print(f"{factorial(3)=}  <-- this should be {math.factorial(6)}")
print(f"{factorial(5)=}  <-- this should be {math.factorial(5)}")
