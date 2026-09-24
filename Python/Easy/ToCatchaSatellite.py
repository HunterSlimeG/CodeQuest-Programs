import sys, math
cases = int(sys.stdin.readline().rstrip())
grav = 0.00000000006673
mass = 5980000000000000000000000
rad_earth = 6370000
for caseNum in range(cases):
    alt = int(sys.stdin.readline().rstrip())
    rad = rad_earth + alt
    vel = math.sqrt((grav * mass) / rad)
    time = round(math.sqrt((4 * math.pow(math.pi, 2) * math.pow(rad, 3)) / (grav * mass)))
    print(round(vel), f"{math.floor(time / 3600)}:{math.floor((time % 3600) / 60):02d}:{math.floor((time % 3600) % 60):02d}")