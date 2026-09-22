import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
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
    words = int(sys.stdin.readline().rstrip())
    for w in range(words):
        word = sys.stdin.readline().rstrip()
        for i, l in enumerate(word):
            if l.upper() in alpha.keys():
                replace = alpha[l.upper()]+"-" if i+1 < len(word) and word[i+1].isspace() else alpha[l.upper()]
                word.replace(l, replace, 1)
        print(word)
            