import sys
cases = int(sys.stdin.readline().rstrip())
vowels = "aeiou"
for caseNum in range(cases):
    count = 0
    for l in sys.stdin.readline().rstrip():
        if l in vowels:
            count += 1
    print(count)