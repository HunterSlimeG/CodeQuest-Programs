
yes = " = ANAGRAM"
no = " = NOT AN ANAGRAM"
cases = int(input())
for caseNum in range(cases):
    line = input()
    words = line.split("|")
    if words[0]==words[1]:
        print(line+no)
    elif sorted(words[0])==sorted(words[1]):
        print(line+yes)
    else:
        print(line+no)