# strong_number.py
# Check whether a number is a Strong number.
# A Strong number is a number in which the sum of the factorial of its digits equals the number itself.

import math


def is_strong_number(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += math.factorial(digit)
        n //= 10
    return total == original


if __name__ == "__main__":
    number = int(input("Enter a number to check for Strong number: "))
    if is_strong_number(number):
        print(f"{number} is a Strong number.")
    else:
        print(f"{number} is not a Strong number.")
