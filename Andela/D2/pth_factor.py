

def pthFactor(n, p):
    factors = []
    index = 1
    to_avoid = set()

    while index <= n and index not in to_avoid:
        if n % index == 0:
            factors.append(index)
        else:
            value = index + index
            while value < n:
                to_avoid.add(value)
                value += index

        if len(factors) == p:
            return index

        index = index + 1

    if p > len(factors):
        return 0

    return factors[p - 1]

if __name__ == '__main__':
    print(pthFactor(30000, 3))