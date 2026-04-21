import sys
cases = int(sys.stdin.readline().rstrip())
smoothies = {
    "strawberry swirl": ["strawberry", "blueberry"],
    "banana burst": ["banana", "kiwi", "orange"],
    "tropical tango": ["kiwi", "orange", "mango", "blueberry"],
    "mango medley": ["mango", "strawberry", "blueberry", "banana"],
}
for caseNum in range(cases):
    ing = sys.stdin.readline().rstrip().split("|")
    smooth = sys.stdin.readline().rstrip()

    can = True
    for i in smoothies[smooth]:
        if not i in ing:
            can = False

    if can:
        print("YES")
    else:
        print("NO")
