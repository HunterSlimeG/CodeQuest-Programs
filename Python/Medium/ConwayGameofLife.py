import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    gens = int(sys.stdin.readline().rstrip())
    board: list[list] = []

    for i in range(10):
        board.append(sys.stdin.readline().rstrip())

    for g in range(gens):
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                pass
                
    
    for row in board:
        print("".join(row))
