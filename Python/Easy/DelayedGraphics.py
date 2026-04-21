import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    max = int(sys.stdin.readline().rstrip())
    delay = sum([int(i) for i in sys.stdin.readline().rstrip().split(" ")])

    if delay>max:
        print(delay-max)
    else:
        print("PASS")
