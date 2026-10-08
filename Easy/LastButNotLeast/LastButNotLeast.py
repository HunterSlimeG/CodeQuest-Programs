
cases = int(input())
for caseNum in range(cases):
    line = input().replace('"', '').replace(" ", "")
    
    if len(line)==0:
        print("No Letter Found")
    else:
        print(line[-1])

