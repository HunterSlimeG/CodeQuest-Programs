
cases = int(input())
for caseNum in range(cases):
    num1, op, num2 = input().split(" ")
    val1 = eval(num1+op+num2)+ 0.000000001
    val2 = eval(num2+op+num1)+ 0.000000001
    print(str(round(val1, 1))+" "+str(round(val2, 1)))
