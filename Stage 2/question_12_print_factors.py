# STAGE 2 - QUESTION - 12
# 12. Print all factors of a number.

"""
A factor of a number N is a smaller number that divides N exactly (with no remainder)

Example:
For 12, the factors are:
1, 2, 3, 4, 6, 12

Reason:

12 % 1  = 0
12 % 2  = 0
12 % 3  = 0
12 % 4  = 0
12 % 6  = 0
12 % 12 = 0

Strategy:
- Take number from user
- Loop from 1 to N
- For each number i, check:

if N % i == 0:
    i is a factor

- Print it
This is very simple And very important as builds the base for:
- Prime checking
- GCD (Greatest common Divisor)
- LCM (Least common multiple)
- Divisor - related math problems

"""

# Take input from the usser
num = int(input("Enter a positive integer: "))

# Print a message
print(f"Factors of {num} are: ")

# Loop from 1 to num
# Every number i in this range is checked to see whether it divides num

for i in range (1, num + 1):
    
    # Check if i is a factor (no remainder)
    if num % i == 0:
        print(i)

"""
Notes:

Complexity 
- This method takes O(N) time, which is fine for beginners.

Faster Way (Advanced Hint)
- You can check only up to sqrt(N) for efficiency - we'll learn that later

Why loop until N ?
- Becuase N itself is always a factor

"""


