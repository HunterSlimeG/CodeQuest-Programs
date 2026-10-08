
cases = int(input())
for caseNum in range(cases):
    cards = []
    for c in range(int(input())):
        cards.append(input())
    
    card = input()
    count = 0
    for i in cards:
        if i==card:
            count += 1
    
    print(count)