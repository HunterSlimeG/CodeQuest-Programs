
cases = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for caseNum in range(cases):
    line = input()
    message = ""
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            if i+1 < len(line) and line[i+1].isnumeric():
                message += (alpha[int(line[i:i+2]) - 1])
                i += 1
            else:
                message += (alpha[int(line[i]) - 1])
        i += 1
    print(message)