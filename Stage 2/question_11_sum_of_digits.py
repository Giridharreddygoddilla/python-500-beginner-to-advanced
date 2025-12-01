# STAGE 2 - QUESTION - 11
# 11. Print the sum of digits of a number.

"""
We want to take a number like:
- 1234 -> 1 + 2 + 3 + 4 = 10
- 5029 -> 5 + 0 + 2 + 9 = 16

We'll do this without converting to string, using pure math (good for logic building).

Key idea:
Use the same pattern you saw before:
-  % 10  -> gives the last digit 
- // 10  -> removes the last digit

Example with 1234:

- 1234 % 10  = 4    -> last digit
- 1234 // 10 = 123  -> remaining number
- 123 % 10 = 3, 123 // 10 = 12 
- 12 % 10 = 2, 12 // 10 = 1
- 1 % 10 = 1, 1 // 10 = 0  -> stop here

We'll:
- Extract each digit with % 10
- Keep adding it to a running sum
- Remove the digit with // 10
- Repeat until the number becomes 0

"""
# Take input from the user
num = int(input("Enter an integer: "))

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Make a copy of the original number (optinal, just for clarity)
# We use 'n' to process the number so that we don't lose the original 'num' value
n = num

# Loop until n becomes 0
# In each iteration:
#  - Extract the last digit using n % 10
#  - Add that digit to sum_of_digits
#  - Remove the last digit from n using integer division n // 10

while n > 0:
    last_digit = n % 10          # extract the last digit
    sum_of_digits += last_digit  # add it to the sum
    n = n // 10                  # remove the last digit

# - Print the result
print(f"The sum of digits of {num} is: {sum_of_digits}")


"""
Notes:
This  % 10 and  // 10 pattern is super important - you'll see it again in:
 - reversing numbers
 - digit - based checks (like Armstrong numbers, palindromes, etc...)
Using a copy n = num helps keep the original value safe for displaying later.

"""