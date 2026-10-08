
cases = int(input())
for caseNum in range(cases):
    list1 = [float(i) for i in input().split(" ")]
    list2 = [float(i) for i in input().split(" ")]
    vals = []
    for n in range(len(list1)):
        if list1[n] >= .6 and list1[n] <= .85 and list2[n] >= .6 and list2[n] <= .85:
            vals.append(n)
    length = len(vals)
    indices = " ".join([str(i) for i in vals])
    if length == 0:
        print("No multipaction events detected.")
    elif length == 1:
        print(f"A multipaction event was detected at time index {vals[0]}.")
    else:
        print(f"{length} multipaction events were detected at time indices: {indices}.")