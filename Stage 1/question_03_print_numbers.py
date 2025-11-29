# STAGE 1 --> QUESTION -3
# 3. Print numbers from 1 to 50 using a loop.

"""
To print numbers from 1 to 50, we need a loop.
Python offers two main types:
- for loop 
- while loop

For this task, for - loop is perfectly suited becuase we know the exact range of numbers.

# Understanding range() function

range(start, stop)
- start --> beginning number
- stop --> ending number( not included)

Example:

So to print 1 to 50:
range(1, 51)

Becuase 51 is not included.

"""
# Use a for loop
for i in range(1, 51):
    print(i)

"""
Explination:
- "i" will take values: 1, 2, 3, 4, ...,50
- print(i) prints each number on a new line

"""

"""
Notes:
- range() is fundamental in loop-based problems.
- Remember: the last number is always excluded.
- Loop variables like i or num are temporary counters.

"""