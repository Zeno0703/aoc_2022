def getScores():
    totalScore = 0
    totalScore2 = 0
    games = createArray()
    for game in games:
        totalScore += chooseWinner(game[0], game[1])
        totalScore2 += chooseWinnerDiff(game[0], game[1])
    return totalScore, totalScore2


def chooseWinner(rps1, rps2):
    if rps1 == 'A':
        if rps2 == 'X':
            return 3 + 1
        elif rps2 == 'Y':
            return 6 + 2
        return 0 + 3
    elif rps1 == 'B':
        if rps2 == 'Y':
            return 3 + 2
        if rps2 == 'X':
            return 0 + 1
        return 6 + 3
    else:
        if rps2 == 'Z':
            return 3 + 3
        elif rps2 == 'X':
            return 6 + 1
        return 0 + 2


def chooseWinnerDiff(rps1, rps2):
    if rps2 == 'X':
        if rps1 == 'A':
            return 0 + 3
        elif rps1 == 'B':
            return 0 + 1
        return 0 + 2
    elif rps2 == 'Y':
        if rps1 == 'A':
            return 3 + 1
        if rps1 == 'B':
            return 3 + 2
        return 3 + 3
    elif rps2 == 'Z':
        if rps1 == 'A':
            return 6 + 2
        elif rps1 == 'B':
            return 6 + 3
        return 6 + 1


def createArray():
    games = open("input.txt", "r")
    gamesArray = []

    for game in games:
        gamesArray.append(game.rstrip('\n').replace(" ", ""))

    return gamesArray


def main():
    score, score2 = getScores()
    print(score, score2)


if __name__ == '__main__':
    main()