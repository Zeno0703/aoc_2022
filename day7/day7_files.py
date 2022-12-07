import re


def main():
    directories = getInput()
    sizes = dict()
    getSizeOfDirs(directories, sizes)
    print(sizes)
    sumOfDirs = 0
    for directory in sizes:
        if sizes[directory] <= 100000:
            print(directory)
            sumOfDirs += sizes[directory]
    print(sumOfDirs)


def getInput():
    directories = dict()
    entries = [entry for entry in open('input.txt').read().splitlines()]

    for i in range(len(entries)):
        if "$ cd" in entries[i] and entries[i] != "$ cd ..":
            name = re.sub(r'.', '', entries[i], count = 5)
            contents = []
            for entry in entries[i+2:]:
                if "$" not in entry:
                    contents.append(entry)
                else:
                    break
            directories[name] = contents

    return directories


def getSizeOfDirs(directories, sizes):
    for direc in directories:
        size = getSize(directories, directories[direc], sizes)
        sizes[direc] = size


def getSize(directories, values, sizes):
    summation = 0
    for i in range(len(values)):
        print(values[i])
        if values[i] in sizes:
            continue
        if "dir" in values[i]:
            summation += getSize(directories, directories[re.sub(r'.', '', values[i], count = 4)], sizes)
        else:
            summation += int(re.findall(r'\d+', values[i])[0])
    return summation


if __name__ == '__main__':
    main()