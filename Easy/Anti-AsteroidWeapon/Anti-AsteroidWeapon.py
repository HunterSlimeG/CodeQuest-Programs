import math
cases = int(input())
for caseNum in range(cases):
    count = int(input())
    
    asteroids = []
    for c in range(count):
        asteroids.append([int(i) for i in input().split(" ")])

    asteroids.sort(key=lambda aster: math.sqrt(math.pow(aster[0], 2) + math.pow(aster[1], 2)))
    print("\n".join([str(a).replace("[", "").replace("]", "").replace(",", "") for a in asteroids]))