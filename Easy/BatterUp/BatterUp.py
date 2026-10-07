import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    name, bats = sys.stdin.readline().rstrip().split(":")
    bats = bats.split(",")
    batNum = len([b for b in bats if b != "BB"])

    slg = (bats.count("1B") + 2 * bats.count("2B") + 3 * bats.count("3B") + 4 * bats.count("HR")) / batNum if batNum > 0 else 0

    print(f"{name}={round(slg, 3):.3f}")