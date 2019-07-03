

def change(value, coins):
    current = set((coin,) for coin in coins)
    done = set()

    while len(current) > 0:
        for set in current:
            current_sum = sum(current[index])

            if current_sum == value:
                done.add(current[index])

            else:
                for coin in coins:
                    if coin + current_sum <= value:
                        original = list(current[index])
                        original.append(coin)
                        current.add(set(original))

            del current[index]
    return done


if __name__ == '__main__':
    print(change(10, [1, 2, 3]))