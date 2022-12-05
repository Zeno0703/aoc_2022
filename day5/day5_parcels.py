parcels = [["CQB"],
           ["ZWQR"],
           ["VLRMB"],
           ["WTVHZC"],
           ["GVNBHZD"],
           ["QVFJCPNH"],
           ["SZWRTGH"],
           ["PZWBNMGC"],
           ["PFQWMBJN"]]

moves = [move for move in open('input.txt').read().splitlines()]
for move in moves:
    numbers = [int(i) - 1 for i in move.replace("move ", "").replace("from ", "").replace("to ", "").split(' ')]
    print(numbers)