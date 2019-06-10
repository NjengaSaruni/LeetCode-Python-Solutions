import unittest


class Compressor(object):
    """
    Wrapper for simple lossless compression operations
    Examples:
        1. Compression
            a. ``abbccc`` becomes ``a1b2c3``
            b. ``aaaaaaaaaaaaaaa`` becomes  `a12`
        2. Decompression, does the opposite of compression
            a. ````
    """

    @classmethod
    def compress(cls, original: str) -> str:
        compressed = ''

        last_character = ''
        count = 0

        # for index in range(len(original) - 1):
        #     if character == last_character:
        #         count += 1
        #     elif last_character != '':


        return compressed


    @classmethod
    def recursive_compression(cls, original: str) -> str:
        return Compressor.recursive_compression_helper(original, 0, 1, '')


    @classmethod
    def recursive_compression_helper(cls, original, index, count, answer):
        if index == len(original) - 1:
            answer += original[index] + str(count)

        elif original[index] == original[index + 1]:
            answer = Compressor.recursive_compression_helper(original, index + 1, count + 1, answer)

        else:
            answer += original[index] + str(count)
            return Compressor.recursive_compression_helper(original, index + 1, 1, answer)

        return answer

if __name__ == '__main__':
    print(Compressor.recursive_compression('aaaaaaaaaabbbccll'))