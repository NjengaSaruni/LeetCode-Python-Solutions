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


def binary_search_recursive(ls, target, left, right):
    mid = (left + right) // 2

    if ls[mid] == target:
        return mid

    if left >= right:
        return -1

    if ls[mid] > target:
        return binary_search_recursive(ls, target, left, mid)
    else:
        return binary_search_recursive(ls, target, mid + 1, right)


if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5, 91]
    print(binary_search(ls, 4))
    print(binary_search_recursive(ls, 4, 0, len(ls)))
