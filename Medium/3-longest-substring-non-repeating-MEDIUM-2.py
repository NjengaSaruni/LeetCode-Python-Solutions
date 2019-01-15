# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = ''

    i = 0
    length = len(s)

    while i < length:
        current = ''
        j = i

        while j < length:
            if s[j] not in current:
                current += s[j]
            else:
                break
            if len(current) > len(longest):
                longest = current

            j += 1
        i += 1

    return len(longest)


if __name__ == '__main__':
    print(lengthOfLongestSubstring('sdabbbbaxasdsadsefdsfscacdfacdaa'))

