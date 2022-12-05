parcels1 = ["BQC",
           "RQWZ",
           "BMRLV",
           "CZHVTW",
           "DZHBNVG",
           "HNPCJFVQ",
           "HGTRWZS",
           "CGMNBWZP",
           "NJBMWQPF"]

parcels2 = ["BQC",
           "RQWZ",
           "BMRLV",
           "CZHVTW",
           "DZHBNVG",
           "HNPCJFVQ",
           "HGTRWZS",
           "CGMNBWZP",
           "NJBMWQPF"]

moves = [move for move in open('input.txt').read().splitlines()]

for move in moves:
    numbers = [int(i) for i in move.replace("move ", "").replace("from ", "").replace("to ", "").split(' ')]
    amount = numbers[0]
    move_from = numbers[1] - 1
    move_to = numbers[2] - 1

    for i in range(amount):
        copy = parcels1[move_from][-1]
        parcels1[move_from] = parcels1[move_from][:-1]
        parcels1[move_to] = parcels1[move_to] + copy
        print(parcels1)

    copy2 = parcels2[move_from][-amount:]
    parcels2[move_from] = parcels2[move_from][:-amount]
    parcels2[move_to] = parcels2[move_to] + copy2
    print(parcels2)