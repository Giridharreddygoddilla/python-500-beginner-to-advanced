# STAGE 2 --> QUESTION 2
# 2. Take a number from the user and print whether it is odd or even.

"""

This question teaches you:
- How to accept numeric input
- How to use conditions (if, else)
- How to use the modulus operator(%)
- basic logic building 

"""
# Understanding the Logic
"""
A number is:
- Even if number % 2 == 0
- Odd otherwise

what is % (modulus)?
- It give the remainder after devidtion of two numbers.
Examples:
- 8 % 2 = 0 -->  even
- 11 % 2 = 1 --> odd
- 27 % 2 = 1 --> odd
- 100 % 2 =0 --> even

Very simple rule:
- If remainder is 0 --> Even
- If remainder is not 0 --> odd

"""

# Take input from the user

# As before, we convert the input string to an ingeger:
num = int(input("Enter a number: "))

# check Even or Odd
# we use an if statement:

if num % 2 == 0:
    print(" The number is Even: ", num)
else:
    print("The number is Odd: ", num)

"""
Notes:

- Always convert input using int()
- Conditions are checked in order
- % is extreamly important for many coding problems
- This question forms the base of bigger logic later

"""