import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    if "blue" in line:
        print("blue")
    elif "red" in line:
        print("red")
    else:
        print("no color found")
