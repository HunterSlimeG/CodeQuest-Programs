
cases = int(input())
for caseNum in range(cases):
    val = int(input())
    fibb = [0, 1]
    while fibb[-1] < val:
        fibb.append(fibb[-1] + fibb[-2])

    print("TRUE" if fibb[-1] == val or val == 0 else "FALSE")