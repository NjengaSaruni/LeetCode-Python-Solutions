import math
import heapq

def minSum(num, k):

    heapq._heapify_max(num)

    while k > 0:
        heapq._heapreplace_max(num, math.ceil(num[0] / 2))
        k -= 1

    return sum(num)

if __name__ == '__main__':
    print(minSum([10, 20, 7], 4))