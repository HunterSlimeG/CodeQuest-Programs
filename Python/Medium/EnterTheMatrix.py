import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    C = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")], [int(i) for i in sys.stdin.readline().rstrip().split(" ")]]
    F = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

    discrimnant = (C[0][0] * C[1][1]) - (C[0][1] * C[1][0])
    invC = [[C[1][1]/discrimnant, -C[0][1]/discrimnant], 
            [-C[1][0]/discrimnant, C[0][0]/discrimnant]]

    E = [invC[0][0]*F[0]+invC[1][0]*F[1], invC[0][1]*F[0]+invC[1][1]*F[1]]
    E = [round(i+0.01) for i in E]
    print(str(E[0]) + " " + str(E[1]))
