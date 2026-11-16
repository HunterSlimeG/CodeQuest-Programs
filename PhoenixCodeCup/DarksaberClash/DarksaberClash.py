cases = int(input())
for caseNum in range(cases):
    x = -1
    y = -1
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(i) for i in input().split(" ")]
    m1 = (y2 - y1) / (x2 - x1) if (x2 - x1) > 0 else None
    m2 = (y4 - y3) / (x4 - x3) if (x4 - x3) > 0 else None

    if (m1 is None and m2 is None) and x1 != x3:
        x = -1
    elif m1 is None and m2 is not None:
        x = x1
    elif m2 is None and m1 is not None:
        x = x3

    if (m1 == 0 and m2 == 0) and y1 != y3:
        y = -1
    elif m1 == 0 and m2 != 0:
        y = y1
    elif m1 != 0 and m2 == 0:
        y = y3

    if m1 == m2:
        x = -1
        y = -1
    