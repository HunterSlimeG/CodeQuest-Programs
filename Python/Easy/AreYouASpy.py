import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    greet, respond = sys.stdin.readline().rstrip().split("|")

    spy = True
    for r in respond:
        if not r.lower() in greet.lower() and r.isalpha():
            spy = False
            break

    print("That's my secret contact!" if spy else "You're not a secret agent!")
    