import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    val = int(sys.stdin.readline().rstrip())
    fibb = [0, 1]
    for v in range(val - 2):
        fibb.append(fibb[-1] + fibb[-2])

    print(f"{val} = {fibb[val - 1] if val > 0 else 0}")