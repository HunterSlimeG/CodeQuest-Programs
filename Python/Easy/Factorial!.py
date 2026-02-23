import sys

def factorial(val, sum=1):
    sum *= val
    if val-1>0:
        return factorial(val-1, sum)
    else:
        return sum

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    print(factorial(int(sys.stdin.readline().rstrip())))
