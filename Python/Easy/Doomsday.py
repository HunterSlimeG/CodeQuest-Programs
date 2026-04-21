import sys, math
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    total = int(sys.stdin.readline().rstrip())
    sizes = []

    while total>0:
        sqrt = math.sqrt(total)
        total -= math.floor(sqrt)**2
        sizes.append(math.floor(sqrt)**2)

    print(sizes)