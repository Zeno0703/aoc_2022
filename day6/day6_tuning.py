def main():
    string = open("input.txt").readline()
    for i in range(len(string)-4):
        if len(set(string[i:i+4])) == 4:
            print(i + 4)
            break

    for i in range(len(string)-14):
        if len(set(string[i:i+14])) == 14:
            print(i + 14)
            break


if __name__ == '__main__':
    main()