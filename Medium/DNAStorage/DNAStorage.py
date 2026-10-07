import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    binLine = ""
    text = ""
    for i in range(len(line)):
        binLine += line[i].replace("A", "0").replace("T", "0").replace("C", "1").replace("G", "1")

    for i in range(len(binLine)//7):
        text += chr(int(binLine[i*7:i*7+7], 2))
    print(text)