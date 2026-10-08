
cases = int(input())
for caseNum in range(cases):
    val = int(input())
    start = val
    count = 1
    while val > 1:
        val = val / 2 if val % 2 == 0 else val * 3 + 1
        count += 1

    print(f"{start}:{count}")
    
    