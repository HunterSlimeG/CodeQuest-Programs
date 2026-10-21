cases = int(input())
for caseNum in range(cases):
    num = int(input())
    ids = [int(i) for i in input().split(" ")]
    for n in range(1, num + 1):
        if not n in ids:
            print(n)