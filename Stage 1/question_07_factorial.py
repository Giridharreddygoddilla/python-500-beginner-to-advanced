#  STAGE 1 --> QUESTION - 7
# 7. Find the factorial of a number.

"""
What is factorial ?
- Factorial of a number N (written as N!) is:
N! = N * (N-1) * (N-2) * ... * 1

Examples:
5! = 5 * 4 * 3 * 2 * 1 = 120
4! = 24
3! = 6
1! = 1
0! = 1 (important special case)

So, our goals:
- Take number from user
- Handle special cases (0! and 1!)
- Use a loop to multiply numbers from 1 to N
- Print the result clearly

"""

# Take numbr input from the user
num = int(input("Enter a number : "))

# Initialixe a variable to hold the factorial result
# We start with 1 becuase factorial multiplication identity is 1.
factorial = 1

# Handle special case 
# If num is 0 or 1, the answe is simply 1.
if num == 0 or num == 1:
    factorial = 1
else:
    # Use a loop to multiply from 2 up to num
    # Example for num = 5: multiply 2 * 3 * 4 * 5
    for i in range(2, num + 1):
        factorial *= i    # Same as : factorial = factorial * i

# Print the final factorial result
print(f"The Factorial of {num} is: {factorial}")

"""
Notes:

Why start factorial at 1 ?
Becuase:
- Multiplying by 0 would zero out everything.
- Multiplying by 1 keeps values intact
- It's the identity element in multiplication.

Why loop from 2 to num ?

- Becuase multiplying by 1 doesn't change anythig. This makes the loop faster and cleaner.

Why handle 0! separately?
0! is defined as 1 (mathematically).

"""