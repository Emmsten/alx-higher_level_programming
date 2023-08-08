#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10
prefix = "and is"

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} {prefix} greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} {prefix} 0")
else:
    print(f"Last digit of {number} is {last_digit} {prefix} less than 6 and not 0")

