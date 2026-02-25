import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    num = sys.stdin.readline().rstrip()
    sum = 0
    for n in range(len(num)-1):
        sum += int(num[n])*(10-n)
    check = 11-(sum%11)
    if str(check)==num[-1] or (check==10 and num[-1]=="X") or (check==11 and num[-1]=="0"):
        print("VALID")
    else:
        print("INVALID")