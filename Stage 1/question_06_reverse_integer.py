# STAGE 1 --> QUESTION - 6
# 6. Reverse an integer (without converting it to a string).

"""
Reversing a number mathematically is a classic logic problem.
It teaches:
- extracting digits
- reconstructing numbers
- using loops effectively
- integer division and modulus

This problem is a foundation for:
- checking numeric palindromes
- understanding number decomposition
- competitive programming logic

# Understand How to Reverse a Number
Example :
Number -> 1234
We want -> 4321

How do we do it ?

We extract digits from the end using   % 10:

1234 % 10 = 4
123 % 10  = 3
12 % 10   = 2
1 % 10    = 1

Then we build a new number using :

reversed_num = reversed_num * 10 + digit

This shifts digits left and adds the new one.

"""
# Take input
num = int(input("Enter a number: "))
# Reverse the integer
# We need:
# - rev = 0 -> stores reversed number
#   n = num -> temporary working variable

rev = 0
n = num

while n > 0:
    digit =  n % 10   # extract last digit
    rev = rev * 10 + digit 
    n = n // 10       # remove last digit 
# print result
print("Reversed Number :", rev)

"""
Notes:
- Never use strings for this problem - this builds core logic.
- Pattern of % 10 and // 10  is  crucial for many future problems.
- Works for any positive integer.
- Later we'll handle negatives and zeros as special cases.

"""
