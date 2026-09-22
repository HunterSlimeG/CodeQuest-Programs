import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    spd, birth = sys.stdin.readline().rstrip().split(" ")
    spd = int(spd)
    if birth == "true":
        if spd <= 65:
            print("no ticket")
        elif spd <= 85:
            print("small ticket")
        else:
            print("big ticket")
    else:
        if spd <= 60:
            print("no ticket")
        elif spd <= 80:
            print("small ticket")
        else:
            print("big ticket")