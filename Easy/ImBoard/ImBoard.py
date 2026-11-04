cases = int(input())
for caseNum in range(cases):
    size = int(input())

    row = ""
    for x in range(size):
        row += "# "
    for y in range(size):
        print(row.strip())
