def is_palindrome(string):

    left = 0
    right = len(string) - 1

    while left <= right and string[left] == string[right]:
        left += 1
        right -= 1

    return left >= right

if __name__ == '__main__':
    print(is_palindrome('aabbaa'))