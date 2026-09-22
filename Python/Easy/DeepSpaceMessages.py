import sys
cases = int(sys.stdin.readline().rstrip())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    nums = []
    for i, l in enumerate(line):
        if l.isnumeric():
            if i+1 < len(line) and line[i+1].isnumeric():
                nums.append(int(line[i:i+1]))
            else:
                nums.append(int(l))