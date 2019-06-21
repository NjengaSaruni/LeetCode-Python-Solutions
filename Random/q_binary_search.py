def binary_search(value, array):
    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    array = [1, 2, 5, 9, 10, 12]

    print(binary_search(10, array))
