def main():
    trees = [i for i in open('input.txt').read().splitlines()]
    visibleEdge = (len(trees) + len(trees[0])) * 2 - 4

    visibleGrid = 0

    for row in range(1, len(trees) - 1):
        for col in range(1, len(trees[0]) - 1):
            if isVisible(trees, row, col):
                visibleGrid += 1

    visible = visibleGrid + visibleEdge
    print(visibleEdge, visibleGrid, visible)


def isVisible(trees, row, col):
    tree = trees[row][col]

    for i in range(row - 1, -1, -1):
        if trees[i][col] >= tree:
            break
    else:
        return True

    for i in range(row + 1, len(trees)):
        if trees[i][col] >= tree:
            break
    else:
        return True

    for neighbour in reversed(trees[row][:col]):
        if neighbour >= tree:
            break
    else:
        return True

    for neighbour in trees[row][col + 1:]:
        if neighbour >= tree:
            break
    else:
        return True

    return False


if __name__ == '__main__':
    main()