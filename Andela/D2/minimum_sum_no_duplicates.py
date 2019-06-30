def getMinimumUniqueSum(arr):
    unique = set()
    duplicates = []

    for character in arr:
        if character in unique:
            duplicates.append(character)
        else:
            unique.add(character)

    duplicates = sorted(duplicates)

    for item in duplicates:
        item = item + 1
        while item in unique:
            item = item + 1

        unique.add(item)

    return sum(unique)

if __name__ == '__main__':
    print(getMinimumUniqueSum([1,2,2,1,1,1,-1]))