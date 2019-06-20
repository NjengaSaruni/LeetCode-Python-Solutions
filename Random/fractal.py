def fractal(folds):
    current = ''

    for i in range(folds):
        previous = current
        current += 'L'
        for j in previous:
            if j == 'L':
                current += 'R'
            else:
                current += 'L'

    return current


if __name__ == '__main__':
    print(fractal(4))
