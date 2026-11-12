cases = int(input())
for caseNum in range(cases):
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(i) for i in input().split(" ")]
    m1 = (y2 - y1) / (x2 - x1) if (x2 - x1) > 0 else False
    m2 = (y4 - y3) / (x4 - x3) if (x4 - x3) > 0 else False