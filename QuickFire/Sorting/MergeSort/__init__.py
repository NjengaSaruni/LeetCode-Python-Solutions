"""
This module contains my quickfire solutions to the mergesort algorithm
"""

def pow(x, y):
    if y == 0:
        return 1

    power = x * pow(x, abs(y) - 1)

    if y < 0 and power != 0:
        power = 1 / power

    return power


if __name__ == '__main__':
    print(pow(0.2, -2))