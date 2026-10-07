import sys
cases = int(sys.stdin.readline().rstrip())
units = ["SECONDS", "MINUTES", "HOURS", "DAYS"]
convUp = [(1/60), (1/60), (1/24), 1]
convDn = [1, 60, 60, 24]
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip().split(" ")
    num, unit1, unit2 = line
    oldNum = line[0]
    oldUnit = line[1]
    num = int(num)
    while units.index(unit1)!=units.index(unit2):
        if units.index(unit1)>units.index(unit2):
            num *= convDn[units.index(unit1)]
            unit1 = units[units.index(unit1)-1]
        else:
            num *= convUp[units.index(unit1)]
            unit1 = units[units.index(unit1)+1]
    print(f"{oldNum} {oldUnit}->{round(num+0.001)} {unit2}")