
cases = int(input())
vowels = "aeiou"
for caseNum in range(cases):
    count = 0
    for l in input():
        if l in vowels:
            count += 1
    print(count)