def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

if __name__ == '__main__':
    print(is_palindrome('aabbaag'))