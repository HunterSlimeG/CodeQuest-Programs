word = input()
n = int(input())
for nn in range(n):
    valid = "YES"
    wrd = input()
    bank = word
    for l in wrd:
        if l in bank:
            bank = bank.replace(l, "", 1)
        else:
            valid = "NO"
            break
    print(valid)