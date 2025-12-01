# STAGE 1 COMPLETED
# 10. Print all even numbers between 1 and N.
"""
We must print all even numbers strings from 1 up to N.

- What makes a number even ?
A number is even if:

number % 2 == 0

Strategy:
- Take input N
- Loop from 1 to N
- Check if each number is even
- Print only even ones

This question builds loop + condition logic skills.

"""
# Take input from the user
N = int(input("Enter a positive integer N: "))

# Loop from 1 to N
for num in range (1, N + 1):

    # Check if the current number is even
    if num % 2 == 0:
        print(num)


"""
Notes:

Why loop from 1 ?
- Becuase problem says 1 to N.

Can we make it more efficient ?
- Yes - instead of checking every number, we can start from 2 and jump by 2.

More efficient method:

for num in range (2, N + 1, 2):
    print(num)


Here:
- 2      -> Starting number
- N + 1  -> ending point
- 2      -> step size (jump by 2 every time)

This avoids unnecessary checks.

"""