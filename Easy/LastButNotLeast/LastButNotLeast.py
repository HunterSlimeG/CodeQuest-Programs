import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip().replace('"', '').replace(" ", "")
    
    if len(line)==0:
        print("No Letter Found")
    else:
        print(line[-1])

