
cases = int(input())
for caseNum in range(cases):
    t, g, h = [int(i) for i in input().split(" ")]
    print(str(t*2+(g+h)*4))
