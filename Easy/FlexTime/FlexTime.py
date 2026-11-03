cases = int(input())
for caseNum in range(cases):
    weeks = int(input())
    hours = 0
    for w in range(weeks):
        hours += sum([int(i) for i in input().split(" ")])
    print(hours - 40)