
cases = int(input())
extensions = {}
for caseNum in range(cases):
    file = input()
    exten = file[file.find(".")+1:]
    if exten in extensions.keys():
        extensions[exten] += 1
    else:
        extensions[exten] = 1

for k in extensions.keys():
    print(k, extensions[k])
