def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right and string[left] == string[right]:
        left += 1
        right -= 1

    return left >= right


def longest_palindromic_substring(string):
    longest = ''

    MAX_LEFT = 0
    MAX_RIGHT = len(string) - 1

    for index, character in enumerate(string):

        # This is the odd iteration
        odd_longest = character
        left = index - 1
        right = index + 1
        while left >= MAX_LEFT and right <= MAX_RIGHT and string[left] == string[right]:
            odd_longest = string[left] + odd_longest + string[right]
            left -= 1
            right += 1

        if len(longest) < len(odd_longest):
            longest = odd_longest

        # This is the even iteration
        if index + 1 <= MAX_RIGHT and string[index + 1] == character:
            even_longest = character + character
            left = index - 1
            right = index + 2

            while left >= MAX_LEFT and right <= MAX_RIGHT and string[left] == string[right]:
                even_longest = string[left] + even_longest + string[right]
                left -= 1
                right += 1

            if len(longest) < len(even_longest):
                longest = even_longest

    return longest


if __name__ == '__main__':
    print(longest_palindromic_substring('aabbaaa'))
