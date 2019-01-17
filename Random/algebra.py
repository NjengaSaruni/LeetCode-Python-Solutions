def algebra(s):
    ans = ''
    value = 0
    for i in s:
        if i.isdigit():
            value = int(i)
        else:
            ans += value * i
            value = 0

    return ans


if __name__ == '__main__':
    print(algebra('1a2b3c'))
