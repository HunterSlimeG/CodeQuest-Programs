import sys
yes = " = ANAGRAM"
no = " = NOT AN ANAGRAM"
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    words = line.split("|")
    if words[0]==words[1]:
        print(line+no)
    elif sorted(words[0])==sorted(words[1]):
        print(line+yes)
    else:
        print(line+no)