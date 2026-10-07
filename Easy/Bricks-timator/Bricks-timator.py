import sys, math
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    total = 0

    inputs = sys.stdin.readline().rstrip().split(" ")
    dims = [int(i) for i in inputs[0].split("x")]
    height = int(inputs[1]) 

    length = 0
    for i in range(int(inputs[2])):
        length += int(inputs[3+i])
    
    total = length/dims[0]
    total *= height/dims[1]

    print(math.ceil(total))
