cases = int(input())
for caseNum in range(cases):
    r, c = [int(i) for i in input().split(",")]
    x1, y1 = [int(i) for i in input().split(",")]
    x2, y2 = [int(i) for i in input().split(",")]

    valid = (((x1 + y1) % 2) == ((x2 + y2) % 2))
    print("Yes" if valid else "No")