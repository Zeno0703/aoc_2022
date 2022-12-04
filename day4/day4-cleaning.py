def main():
    pairs = [pair for pair in open('input.txt').read().splitlines()]
    count, count2 = 0, 0

    for pair in pairs:
        numbers = [int(i) for i in pair.replace(",", '-').split('-')]
        areas1, areas2 = set([i for i in range(numbers[0], numbers[1] + 1)]), set(
            [j for j in range(numbers[2], numbers[3] + 1)])

        if areas1.intersection(areas2) == areas2 or areas2.intersection(areas1) == areas1:
            count += 1

        if areas1.intersection(areas2) != set() or areas2.intersection(areas1) != set():
            count2 += 1

    print(count)
    print(count2)


if __name__ == '__main__':
    main()