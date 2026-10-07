import sys, math
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    count = int(sys.stdin.readline().rstrip())
    
    asteroids = []
    for c in range(count):
        asteroids.append([int(i) for i in sys.stdin.readline().rstrip().split(" ")])

    asteroids.sort(key=lambda aster: math.sqrt(math.pow(aster[0], 2) + math.pow(aster[1], 2)))
    print("\n".join([str(a).replace("[", "").replace("]", "").replace(",", "") for a in asteroids]))