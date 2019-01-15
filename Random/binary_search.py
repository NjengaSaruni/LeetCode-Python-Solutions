def binary_search(ls, target):
    left = 0
    right = len(ls)

    while left < right:
        mid = (left + right) // 2
        if ls[mid] == target:
            return mid
        elif ls[mid] > target:
            right = mid
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 9], 7))
