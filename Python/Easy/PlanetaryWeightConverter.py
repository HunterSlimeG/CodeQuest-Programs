import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    planets = {
        "Mercury": 0.377,
        "Venus": 0.905,
        "Earth": 1,
        "Mars": 0.379,
        "Jupiter": 2.528,
        "Saturn": 1.065,
        "Uranus": 0.886,
        "Neptune": 1.137,
    }
    weight = int(sys.stdin.readline().rstrip())

    for p, m in planets.items():
        mass = round((weight*m)+.00001, 1)
        print(f"{p}: {mass}")
