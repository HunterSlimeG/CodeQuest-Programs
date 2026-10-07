import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    list1 = sys.stdin.readline().rstrip().split(",")
    list2 = sys.stdin.readline().rstrip().split(",")
    group1 = []
    group2 = []
    group3 = []
    for p in list1:
        if p in list2:
            group2.append(p)
            list2.remove(p)
        else:
            group1.append(p)
    group3 = list2
    group1.sort()
    group2.sort()
    group3.sort()
    print(",".join(group1))
    print(",".join(group2))
    print(",".join(group3))