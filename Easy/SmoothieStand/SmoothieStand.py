
cases = int(input())
smoothies = {
    "strawberry swirl": ["strawberry", "blueberry"],
    "banana burst": ["banana", "kiwi", "orange"],
    "tropical tango": ["kiwi", "orange", "mango", "blueberry"],
    "mango medley": ["mango", "strawberry", "blueberry", "banana"],
}
for caseNum in range(cases):
    ing = input().split("|")
    smooth = input()

    can = True
    for i in smoothies[smooth]:
        if not i in ing:
            can = False

    if can:
        print("YES")
    else:
        print("NO")
