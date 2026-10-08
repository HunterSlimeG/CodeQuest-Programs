
cases = int(input())
for caseNum in range(cases):
    gens = int(input())
    board: list[list] = []

    for i in range(10):
        board.append(input())

    for g in range(gens):
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                pass
                
    
    for row in board:
        print("".join(row))
