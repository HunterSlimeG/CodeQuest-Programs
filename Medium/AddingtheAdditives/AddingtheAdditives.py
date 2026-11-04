cases = int(input())
for caseNum in range(cases):
    printers = {}
    jobs = {}
    nump, numj = [int(i) for i in input().split(" ")]
    for p in range(nump):
        line = input().split(" ")
        printers[line[0]] = [float(line[1]), float(line[2])]

    for j in range(numj):
        line = input().split(" ")
        needed = printers[line[0]][0] * float(line[1]) * float(line[2])
        print(int(printers[line[0]][1] // needed))