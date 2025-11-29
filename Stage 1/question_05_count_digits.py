#  STAGE 1 --> QUESTION -5
# 5. Count the number of digits in a number (without converting to string).

"""
This is an import question becuase it teaches you:
- how to work without strings(pure math)
- How to use loops for number processing
- How integer division works

And you will use this skill in many future problems like reversing a number, checking palindrome, etc.

"""
"""
# Logic Understanding  
- To count digits mathematically:
Example: num = 4567

We can continuously divide by 10:

4567 -> 456 -> 45 -> 4 -> 0

Each division removes the last digit.
- We count how many steps until it becomes 0.

"""
# Take input
num = int(input("Enter a Number: "))

# Use a loop to Divide by 10

# We need two variable:
# - count -> counts digits
# - n -> temporary copy of the number

count = 0
n = num

# Loop until n becomes 0:

while n > 0:
    n = n // 10 # remove last digit
    count = count + 1

# - // is integer division , meaning it removes decimals.


# Print the result
print("Number of digits: ", count)


"""
Notes:
- No strings allowes -> good practice for math- based logic
- n // 10 is the key operation
- Works for any positive integer
- Later we will handle negative numbers too.

"""