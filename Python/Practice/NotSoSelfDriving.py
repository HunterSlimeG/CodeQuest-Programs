import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    inps = sys.stdin.readline().rstrip().split(":")
    speed = float(inps[0])
    dist = float(inps[1])
    if speed>0:
        time = dist/speed
        if time<=1:
            print("SWERVE")
        elif time<=5:
            print("BRAKE")
        else:
            print("SAFE")
    else:
        print("SAFE")