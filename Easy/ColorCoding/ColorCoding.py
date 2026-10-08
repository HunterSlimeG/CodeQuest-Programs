
cases = int(input())
for caseNum in range(cases):
    line = input()
    if "blue" in line:
        print("blue")
    elif "red" in line:
        print("red")
    else:
        print("no color found")
