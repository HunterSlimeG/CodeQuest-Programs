ns = int(input())
dict = {}
for n in range(ns):
    line = input().split(" ", 1)
    dict[line[1]] = int(line[0])
print(dict)

qs = int(input())
for q in range(qs):
    word = input()
    if word in dict.keys():
        print(dict[word])
    else:
        print(-1)
