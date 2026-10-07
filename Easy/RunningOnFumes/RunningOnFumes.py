import sys
cases = int(sys.stdin.readline().rstrip())
mpg = {
    4: {"C": 28, "H":35, "O":20},
    6: {"C": 22, "H":28, "O":15},
    8: {"C": 18, "H":22, "O":12}, 
}
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip().split(" ")
    cyl = int(line[0])
    cGas = float(line[1])
    mGas = float(line[2])
    segm = int(line[3])

    for s in range(segm):
        seg = sys.stdin.readline().rstrip().split(" ")
        len = int(seg[1])

        empg = mpg[cyl][seg[0]] - (0.25 * (mGas - cGas))
        cGas -= len/empg
    
    if cGas>=0:
        print("YES")
    else:
        print("NO")