import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    t, g, h = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    print(str(t*2+(g+h)*4))
