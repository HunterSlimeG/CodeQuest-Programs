import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    cards = []
    for c in range(int(sys.stdin.readline().rstrip())):
        cards.append(sys.stdin.readline().rstrip())
    
    card = sys.stdin.readline().rstrip()
    count = 0
    for i in cards:
        if i==card:
            count += 1
    
    print(count)