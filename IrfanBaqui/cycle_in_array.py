"""
Problem Definition:
Given an array in which the value stored as an index is the value of the next index
to go to in the array, write an algorithm to detect if there is loop in this array

Example:
    :args [1, 2, 8, 1, 2, 3, 1, 3, 2]
    :returns: 2
    :description
        Indexes 2 and 8 cause a loop

"""
from typing import List


def circular_array(array: List[int]) -> bool:
    if len(array) <= 1:
        return False

    slow = array[0]
    fast = array[1]

    while 0 < slow < len(array) - 1:
        for i in range(2):
            if fast == slow:
                return True
            if fast == len(array):
                return False

            fast = array[fast]

        slow = array[slow]

    return False


if __name__ == '__main__':
    print(circular_array([1, 2, 3, 4, 3]))
