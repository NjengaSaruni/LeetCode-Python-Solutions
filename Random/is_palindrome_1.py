def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right and string[left] == string[right]:
        left += 1
        right -= 1

    return left >= right


def longest_palindromic_substring(s):
    longest = ''

    MAX_LEFT = 0
    MAX_RIGHT = len(s) - 1

    for index, character in enumerate(s):

        # This is the odd iteration
        odd_longest = middle_out(MAX_LEFT, MAX_RIGHT, character * 2, index, index - 1, index + 1, s)

        if len(longest) < len(odd_longest):
            longest = odd_longest

        # This is the even iteration
        if index + 1 <= MAX_RIGHT and s[index + 1] == character:
            even_longest = middle_out(MAX_LEFT, MAX_RIGHT, character * 2, index, index - 1, index + 2, s)

            if len(longest) < len(even_longest):
                longest = even_longest

    return longest


def middle_out(MAX_LEFT, MAX_RIGHT, even_longest, index, left, right, s):
    while left >= MAX_LEFT and right <= MAX_RIGHT and s[left] == s[right]:
        even_longest = s[left] + even_longest + s[right]
        left -= 1
        right += 1
    return even_longest


if __name__ == '__main__':
    print(longest_palindromic_substring('abba'))
