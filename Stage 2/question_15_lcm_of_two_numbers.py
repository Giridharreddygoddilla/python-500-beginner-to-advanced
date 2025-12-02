# STAGE 2 -> QUESTION - 15
# 15. Find the LCM ( Least Common Multiple) of two numbers.

"""
What is LCM ?
The Least Common Multiple (LCM) of two numbers is:
- The smallest number that is a multiple of both numbers.
Example:
For 4 and 6:

Multiples of 4 -> 4, 8, 12, 16, ...
Multiples of 6 -> 6, 12, 18, 24, ...

Common multiple -> 12, 24, .....

Smallest = 12 -> LCM = 12
"""

"""
Method 1: (Beginner - Friendly)


We keep increasing a number starting from the maximum of the two numbers until we
fine one that both numbers divide exactly.

Example: LCM(4, 6):

Start from max(4, 6) = 6

Check:
- 6 % 4 -> NOT divisible 
- 7 % 4, 7 % 6 -> NOT divisible
- 8, 9, 10, 11 -> NOT divisible

- 12 % 4 == 0 AND 12 % 6 == 0 --> LCM 12
This is the simplest logic for beginners.


Method 2: (Efficient Formula - used in DS & ML)

LCM(a, b) = (a * b)/GCD(a, b)

We will learn GCD in Question 16( Euclid's method).

But for now, we'll go with the beginner method. 

"""

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Start checking from the larger of the two numbers
start = max(num1, num2)

# Loop until we find the LCM
while True:
    # Check if "start" is divisible by both num1 and num2
    if start % num1 == 0 and start % num2 == 0:
        lcm = start    # Found the LCM
        break          # Exit the Loop
    start += 1         # Otherwise, keep searching

# Print the result
print(f"The LCM of {num1} and {num2} is: {lcm}")

"""
Notes:
Why start from max(num1, num2) ?
- Becuase LCM cannot be smaller than the largest number.

Why infinite loop (While True) ?
- We break out as soon as the answer is found.

Why check using % ?
- Divisible exactly means :

number % divisor == 0

More efficient method is coming next 
- When you learn GCD (question 16) using Euclid's alogithm,
your LCM will become ultra-fast using:

LCM = (num1 * num2) // GCD

But you must learn fundamentals first - which you are doing perfectly.

"""