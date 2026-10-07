import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    money = sys.stdin.readline().rstrip()
    cash = float(money.replace("$", ""))

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while cash > 0.001:
        cash = round(cash, 2)
        if cash >= .25:
            cash -= .25
            quarters += 1
        elif cash >= .10:
            cash -= .10
            dimes += 1
        elif cash >= .05:
            cash -= .05
            nickels += 1
        elif cash >= .01:
            cash -= .01
            pennies += 1
        else:
            break

    print(money)
    print(f"Quarters={quarters}")
    print(f"Dimes={dimes}")
    print(f"Nickels={nickels}")
    print(f"Pennies={pennies}")
