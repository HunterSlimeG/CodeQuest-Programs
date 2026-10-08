
cases = int(input())
for caseNum in range(cases):
    list1 = input().split(",")
    list2 = input().split(",")
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