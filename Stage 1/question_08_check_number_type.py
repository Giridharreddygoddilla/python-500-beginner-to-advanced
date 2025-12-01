# STAGE - 1 --> QUESTION - 8
# 8. Check if a number is positive, negative, or zero.
"""
This problem teaches:
- Conditional statements (if, elif, else)
- Comparison operators (>, <, ==)
- Basic decison-making logic

Logic:
- If number is greater than 0 -> itt is positive
- If number is less than 0 -> it is negative
- If number is equal to 0 -> it is zero

Very simple but very important for understanding conditions.

"""
# Take input from the user
num = int(input("Enter a number: "))

# Check whether the number is positive , negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


"""
Notes:
Why use elif instead of another if ?

Becuase:
- 'elif' makes conditions mutually exclusive
- Python stops checking once one condition is true
- It is more efficient and clean


Why check zero last?

Becuase:
- If the number isn't > 0
- And isn't < 0
- Then the only remaining possibility is 0
So else is perfect.

"""
