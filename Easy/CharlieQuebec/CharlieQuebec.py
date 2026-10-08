
cases = int(input())
alpha = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
}
for caseNum in range(cases):
    words = int(input())
    icaoStrings = []
    for w in range(words):
        baseword = input()
        newword = ""
        for i, l in enumerate(baseword):
            if l.upper() in alpha.keys():
                replace = alpha[l.upper()]+"-" if i+1 < len(baseword) and not baseword[i+1].isspace() else alpha[l.upper()]+" "
                newword += replace
        icaoStrings.append(newword)        
    print("\n".join(icaoStrings))
            