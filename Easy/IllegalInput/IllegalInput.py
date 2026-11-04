import re
cases = int(input())
blocked = [r"';.*--", "' OR 1=1", r"\$\{.*\}", r"\$\(.*\)", "&& sudo", "&& su -", ";;", "<script", "%s", "%x", "%n"]
for caseNum in range(cases):
    line = input()
    for b in blocked:
        search = re.search(b, line, flags=re.IGNORECASE)
        if search and search.group():
            print("REJECTED")
            break
    else:
        print(line)