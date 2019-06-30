import math

def minSum(num, k):
    # Perform while k still has a value
    while k > 0:
        highest = max(num)
        num[num.index(highest)] = math.ceil(highest / 2)
        k -= 1

    return sum(num)

if __name__ == '__main__':
    print(minSum([10, 20, 7], 4))