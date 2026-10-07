import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    v1, m1, v2, m2 = [float(i) for i in sys.stdin.readline().rstrip().split(",")]

    finalV = (m1 * v1 + m2 * v2) / (m1 + m2)
    print(f"{finalV:.2f}")
