# STAGE 1 -> QUESTION - 13
# 13. Check whether a number is prime or not.

"""
A prime number is a number that has :

Exactly  two factors: 1 and itself
Examples:
- 2  -> prime
- 3  -> prime
- 5  -> prime
- 7  -> prime
- 11 -> prime

NOT prime (composite):
- 1, 4, 6, 8, 9, 10, 12 ....

# Important:
- 1 is Not a prime 
- 2 is the smallest prime

"""

"""
Logic To Check Prime:

To check if a number N is prime:
- If N <= 1 -> NOT Prime
- Loop from 2 to N-1
- Check if any number divides N
- If any divisor found  -> NOT prime
- If no divisor found -> Prime

This is the beginner method, needed to build intuition.
Later, we will learn the optimized sqrt(N) Method.

"""

# Take  input from the user
num = int(input("Enter a number: "))

# Handle special cases
# 0, 1, and negative numbers are NOT prime
if num <= 1:
    print(f"{num} is NOT a Prime Number.")
else: 
    # Assume the number is prime intially.
    is_prime = True

    # Try dividing num by every number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            # If we find a divisor, it's not prime
            is_prime = False
            break
    # Print Result
    if is_prime:
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")
    
"""
Notes:

Why assume is_prime = True ?
- We assume it's prime until proven otherwise.
- This is a commn pattern in programming:
    Assume success -> search for failure.

Why break the loop early ?
- If we find one divisor, the number is already NOT prime.
- No need to check further -> improves efficiency.

Why treat numbers <= 1 separately ?
- Because they are not prime by definition. 

"""

