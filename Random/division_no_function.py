"""
1 - 1
2 - 4
3 - 9
4 - 16
5 - 25
6 - 36
7 - 49
8 - 64
10 - 100
16 - 256

1.
256 / 2 =  128
128 // 2 = 64
64 // 2 = 32
32 // 2 = 16

2.
9 // 2 = 5
5 // 2 = 3

3.

100 // 2 = 50
50 // 2 = 25
25 // 2 = 13
13 // 2 = 7
20 // 2 = 10

4.
49 // 2 = 25
25 // 2 = 13
13 // 2 = 7


5.

400 // 2 = 200 -> 40000
199 // 2 = 99 -> 9801
98 // 2 = 49 -> 2401
48 // 2 = 24 -> 576
23 // 2 = 11 -> 121
(23 + 11) // 2 = 17 -> 289
(23 + 17) // 2 = 20 -> 400


6.

1000 // 2 = 500 -> 250000
499 // 2 = 249 -> 62001
248 // 2 = 124 -> 15376
123 // 2 = 61 -> 3721
60 // 2 = 30 -> 900
(60 + 30) // 2 = 45 -> 2025
44 // 2 = 22 -> 484
(44 + 22) // 2 = 33 -> 1089
32 // 2 = 16 -> 256
(32 + 16) // 2 = 24 -> 576
(32 + 24) // 2 = 28 -> 784
(32 + 28) // 2 = 30 -> 900
(32 + 30) // 2 = 31 -> 961
(32 + 31) // 2 = 31.5 -> 992.25

9

[1,2,3,4,5,6,7,8,9]
[24,4,7]

"""

import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def square_root(square):
    root = 1

    for i in range(square // 2):
        if square == 1:
            break
        if is_prime(i):
            while square % i == 0:
                if square % (i * i) == 0:
                    square /= (i * i)
                    root *= i
                else:
                    return 1

        else:
            continue

    return root


def _square_root(square):
    factored = math.ceil(square / 2)
    previous_factored = factored
    previous_previous_factored = previous_factored

    while factored ** 2 > square or previous_factored ** 2 > square or previous_previous_factored ** 2 > square:
        if factored ** 2 == square:
            return factored

        if factored ** 2 > square:
            previous_previous_factored = previous_factored
            previous_factored = factored
            factored = math.ceil(factored / 2)

        elif previous_factored ** 2 > square:
            hold = factored
            factored = math.ceil((factored + previous_factored) / 2)
            previous_previous_factored = previous_factored
            previous_factored = hold

        elif previous_previous_factored ** 2 > square:
            hold = factored
            factored = math.ceil((factored + previous_previous_factored) / 2)
            previous_previous_factored = previous_factored
            previous_factored = hold

    return False


if __name__ == '__main__':
    print(square_root(79423744))
