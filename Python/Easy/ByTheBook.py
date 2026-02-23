import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    num = sys.stdin.readline().rstrip()
    index = 10
    sum = 0
    for n in range(len(num)-1):
        sum += int(num[n])*index
        index -= 1
    if str(11-(sum%11))==num[-1] or (11-(sum%11)==10 and num[-1]=="X"):
        print("VALID")
    else:
        print("INVALID")