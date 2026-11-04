cases = int(input())
for caseNum in range(cases):
    vol, fill, leak = [int(i) for i in input().split(" ")]
    waste = int(((vol/(fill - leak)) * leak) + 0.5)
    print(waste)
