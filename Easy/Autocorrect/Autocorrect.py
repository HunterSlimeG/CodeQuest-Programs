cases = int(input())
for caseNum in range(cases):
    dct, wrds = [int(i) for i in input().split(" ")]

    words = {}
    for d in range(dct):
        words[input()] = 0

    for w in range(wrds):
        new = {key: 0 for key in words}
        words = new
        wrd = input()
        for d in words.keys():
            for i in range(len(wrd)):
                if i < len(d):
                    if wrd[i] != d[i]:
                        words[d] += 1
                else:
                    words[d] += 2
            if len(wrd) == len(d):
                words[d] -= 1

        sortedwords = dict(sorted(words.items(), key=lambda item: item[1]))
        print(sortedwords)
        print(list(sortedwords.keys())[0], list(sortedwords.values())[0])