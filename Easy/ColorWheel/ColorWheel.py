
cases = int(input())
mixes = {
    "violet":["blue", "red"],
    "orange":["red", "yellow"],
    "green":["blue", "yellow"],
}
for caseNum in range(cases):
    color = input()
    printed = False
    for k in mixes.keys():
        if k in color:
            printed = True
            print(f"In order to make {color}, {mixes[k][0]} and {mixes[k][1]} must be mixed.")

    if not printed:
        print(f"No colors need to be mixed to make {color}.")
