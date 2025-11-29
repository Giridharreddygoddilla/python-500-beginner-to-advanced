# STAGE 1 --> QUESTION - 1

# 1. Take two numbers as input and print their sum.
"""
Understanding the Problem:
We need to :
1. Ask the user for the first number
2. Ask the user for the second number
3. Add the two numbers
4. Print the result

It looks simple, but there is one very important detail:
--> "input()" always gives a STRING, not a number.

Example:
if the user types: 5
python gets: "5" (string)

So we must convert it.
"""


# We use int() to convert a string to an integer.
num1 = int(input(" Enter the First number: "))
num2 = int(input(" Enter the Second number: "))
# Now num1 and num2  actually contain numbers we can add.

# Add the Two numbers
total = num1 + num2

# Print the Result
print("The sum is:", total)

"""
input() --> recives user input
int() --> converts the input to numbers
+ --> performs addition
print() --> displays output

"""