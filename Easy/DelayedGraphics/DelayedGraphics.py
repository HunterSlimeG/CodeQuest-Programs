
cases = int(input())
for caseNum in range(cases):
    max = int(input())
    delay = sum([int(i) for i in input().split(" ")])

    if delay>max:
        print(delay-max)
    else:
        print("PASS")
