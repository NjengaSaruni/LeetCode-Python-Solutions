if __name__ == '__main__':
    cities = [1000.0, -9, -9, 9999, -6, -9, -8, 999]
    left = 0
    right = len(cities) - 1
    highest = -1000000000

    while left <= right:
        left_appeal = cities[left]
        right_appeal = cities[right]

        twice_left = left_appeal * 2
        twice_right = right_appeal * 2
        left_right = left_appeal + right_appeal + right - left

        highest = max([highest, max([twice_left, twice_right, left_right])])

        if left_appeal > right_appeal:
            right -= 1
        else:
            left += 1

    print(highest)
