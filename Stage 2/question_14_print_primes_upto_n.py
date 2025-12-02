# STAGE 2 -> QUESTION - 14
# 14. Print all Prime numbers between 1 and N.

"""
To print all prime between 1 and N, we must:
- Take N from user
- Loop through every number from 2 to N
- Check for each number if it's prime
- Print only those that are prime

This question reinforces:
- nested loops
- prime logic
- efficient thinking

Prime Checking Recall

A number is prime if:
- It is greater than 1
- It has no divisors from 2 to num -1
We will reuse the same logic from Question 13.

"""

# Take input from the user 
N = int(input("Enter a positive integer N: "))

print(f"Prime numbers between 1 and {N} are: ")

# Loop through all numbers from 2 to N
for num in range(2, N + 1):
   
    # Assume num is prime initially
    is_prime = True
    
    # Check if num has only divisor
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Found a divisor -> Not Prme
            break             # No need to check further
    if is_prime:
        print(num)

"""
Notes:

Why start from 2 ?
Becuase: 
- 0 and 1 are NOT prime
- 2 is the first prime

Why nested loops?
- Outer loop -> picks each number
- Inner loop checks if it's prime

Efficiency (for future)
Checking divisors up to num-1 is simple but slow.
Later, we will learn:
- check only up to sqrt(num)
- Sieve of Eratosthenes(very fast)

For now, focus on logic building.

"""