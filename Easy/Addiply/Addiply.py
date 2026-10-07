import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    val1, val2 = sys.stdin.readline().rstrip().split(" ")
    print(int(val1)+int(val2), int(val1)*int(val2))