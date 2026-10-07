import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    n1, n5, length = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    while length>=5 and n5>0:
        length -= 5
        n5 -= 1
    if length<=n1:
        print("true")
    else:
        print("false")
