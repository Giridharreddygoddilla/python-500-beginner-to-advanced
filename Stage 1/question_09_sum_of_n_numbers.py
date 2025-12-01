# STAGE - 1 --> QUESTION - 9
# 9. Find the sum of the first N natural numbers.

"""
What are Natural numbers ?

Natural numbers are:
1, 2, 3, 4, 5, 6, ...... up to N

we need to calculate:
sum = 1 + 2 + 3 + ..... + N

These are two main ways:

Method 1 (Beginner way): Using a loop
This helps you practice loops and accumulation.

Steps:
- Start sum at 0
- Loop from 1 to N
- Add each number to sum

Method 2 (Advanced & Faster): Using Formula

Mathematically,
sum = N * (N + 1) / 2

We will also show this.
"""

# Take input from User
N = int(input("Enter a positive interger N: "))

# Initialize sum to 0 (starting point)
total_sum = 0

# Loop from 1 to N and add each number to total_sum
for i in range(1, N + 1):
    total_sum += i       # same as total_sum = total_sum + i

# print the result of loop method
print(f"Sum using Loop = {total_sum}")

# Optional : using the mathematical formula (faster way)

formula_sum = N * (N + 1) // 2 # integer division

print(f"Sum using formula = {formula_sum}")

"""
Notes:
Why use // instead of / ?
- // means integer division 
- It avoid decimals
- The sum of natural numbers is always an integer

Why show both methods ?
You must know:
- Loop method -> basics of iteration
- Formula method  - > optimized thinking (important for interviews)

"""