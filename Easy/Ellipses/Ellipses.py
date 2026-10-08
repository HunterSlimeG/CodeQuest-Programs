import math
cases = int(input())

def distance(x, y, x2, y2):
    return math.sqrt(math.pow(x - x2, 2) + math.pow(y - y2, 2))

for caseNum in range(cases):
    x1, y1, x2, y2, w, n = input().split(" ")
    dist = distance(x1, y1, x2, y2)
    points = [False] * n
    for i in range(n):
        x, y = input().split(" ")
