def first(content):
    summation = 0

    for c in content:
        left, right = c[:int((len(c) / 2))], c[int((len(c) / 2)):]

        for letter in left:
            if right.find(letter) != -1:
                if letter.isupper():
                    summation += ord(letter) - 38
                    break
                summation += ord(letter) - 96
                break

    print(summation)


def second(content):
    summation = 0

    for i in range(0, len(content), 3):
        firstL, secondL, thirdL = content[i], content[i + 1], content[i + 2]

        for letter in firstL:
            if secondL.find(letter) != -1 and thirdL.find(letter) != -1:
                if letter.isupper():
                    summation += ord(letter) - 38
                    break
                summation += ord(letter) - 96
                break

    print(summation)


def main():
    content = [letter for letter in open('input.txt').read().splitlines()]
    first(content)
    second(content)


if __name__ == '__main__':
    main()