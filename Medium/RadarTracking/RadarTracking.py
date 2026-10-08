import math
cases = int(input())
for caseNum in range(cases):
    ang1, dist1, ang2, dist2 = [int(i) for i in input().split(" ")]

    x1 = math.sin(math.radians(ang1)) * dist1
    y1 = math.cos(math.radians(ang1)) * dist1

    x2 = math.sin(math.radians(ang2)) * dist2
    y2 = math.cos(math.radians(ang2)) * dist2

    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    speed = round(distance * 10)
    heading = round(math.degrees(math.atan2((y2 - y1), (x2 - x1))))

    print(speed, heading)
