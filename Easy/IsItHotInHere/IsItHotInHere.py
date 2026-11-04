cases = int(input())
for caseNum in range(cases):
    cons = int(input())
    for con in range(cons):
        val, scale = input().split(" ")
        val = float(val)
        if scale == "F":
            print(val, "F", "=", round((val - 32) * (5 / 9), 1), "C")
        elif scale == "C":
            print(val, "C", "=", round((val * (9 / 5)) + 32, 1), "F")
