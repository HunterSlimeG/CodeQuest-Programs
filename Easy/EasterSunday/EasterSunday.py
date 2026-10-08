import math
cases = int(input())
for caseNum in range(cases):
    y = int(input())
    a = y % 19
    b = y % 4
    c = y % 7
    k = math.floor(y / 100)
    p = math.floor((13 + 8 * k) / 25)
    q = math.floor(k / 4)
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    f = (11 * m + 11) % 30
    month = 3 if (22 + d + e) <= 31 else 4
    day = (22 + d + e) % 31
    if d == 28 and e == 6 and f < 19 and month == 4 and day == 25:
        day = 18
    elif d == 29 and e == 6 and month == 4 and day == 26:
        day = 19
    print(f"{y:04d}/{month:02d}/{day:02d}")
