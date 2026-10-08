
cases = int(input())
for caseNum in range(cases):
    words = input().replace("-", " ").split(" ")
    tla = ""

    for w in words:
        for l in w:
            if l.isalpha():
                tla += l
                break
    
    print(tla.upper())
