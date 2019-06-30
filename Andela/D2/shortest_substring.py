def shortestSubstring(s):
    chars = set([char for char in s])

    last_seen = [-1 for _ in range(26)]
    seen = set()
    length = len(s)

    for i in range(len(s)):
        seen.add(s[i])
        last_seen[ord(s[i]) - 97] = i

        if seen == chars:
            left = min([element for element in last_seen if element != -1])
            right = max([element for element in last_seen if element != -1])
            new = right - left + 1
            if new < length:
                length = new

    return length

if __name__ == '__main__':
    print(shortestSubstring('dabbcafbcdzabcdez'))