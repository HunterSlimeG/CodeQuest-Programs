
cases = int(input())
for caseNum in range(cases):
    val = int(input())
    fibb = [0, 1]
    for v in range(val - 2):
        fibb.append(fibb[-1] + fibb[-2])

    print(f"{val} = {fibb[val - 1] if val > 0 else 0}")