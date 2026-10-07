import sys
cases = int(sys.stdin.readline().rstrip())
extensions = {}
for caseNum in range(cases):
    file = sys.stdin.readline().rstrip()
    exten = file[file.find(".")+1:]
    if exten in extensions.keys():
        extensions[exten] += 1
    else:
        extensions[exten] = 1

for k in extensions.keys():
    print(k, extensions[k])
