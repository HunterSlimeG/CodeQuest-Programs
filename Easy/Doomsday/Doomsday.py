import math
cases = int(input())
for caseNum in range(cases):
    total = int(input())
    sizes = []

    while total>0:
        sqrt = math.sqrt(total)
        total -= math.floor(sqrt)**2
        sizes.append(math.floor(sqrt)**2)

    print(sizes)