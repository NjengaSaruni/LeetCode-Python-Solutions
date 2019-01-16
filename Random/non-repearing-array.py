# [1, 2, 3, 3, 4, ]
def non_repeating_array(ls):
    slow = 0
    fast = 1

    while fast < len(ls):
        if ls[slow] == ls[fast]:
            fast += 1
        else:
            slow += 1
            ls[slow] = ls[fast]
            fast += 1

    if len(ls) == 0:
        return slow
    else:
        return slow + 1


if __name__ == '__main__':
    ls = [1, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9]
    val = non_repeating_array(ls)
    print(ls)
    print(val)

