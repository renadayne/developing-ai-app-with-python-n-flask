"""Sample using pylint to check code PEP
   
   pip install pylint
   
   Run pylint sample1.py to check code point (maximum 10)

"""

# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    """Returns the sum of two numbers"""
    return number1 + number2

# Initialize the variable 'NUM1' with the value 4.
NUM1 = 4

# Initialize the variable 'NUM2' with the value 5.
NUM2 = 5

# sum NUM1 and NYM2
TOTAL = add(NUM1, NUM2)

# Print the result of adding 'NUM1' and 'NUM2' using the 'format' method.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
