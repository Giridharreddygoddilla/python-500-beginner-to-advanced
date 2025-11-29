# STAGE 1 --> QUESTION - 4
# 4. Print the multiplication table of any number (1 - 20).

"""
This question teaches you:
- How to take input
- How to use loops
- How to format output
- Simple arthimetic inside loops

"""

# Take input
# We ask the user for a number whose table they want:
num = int(input("Enter a number: "))

# Multilication Table logic

"""
A Multiplication table is:
num * 1
num * 2
num * 3
...
num * 10

So we need to loop from 1 to 20
"""
# Use a for loop

for i in range(1, 21):
    print(num, " X ", i, " = ", num * i)




# Cleaner formatting Using f-strings

# print(f"{num} X {i} = {num * i}")")

# This is more professional and readable.


"""
Notes:
- This type of loop is extremely common in interviews.
- f-strings are preferred for clean printing.
- You can later extend this to tables 1-20 or custom ranges.

"""