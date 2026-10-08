
cases = int(input())
for caseNum in range(cases):
    list = input().split(" ")
    dirs = "NWSE"
    x = int(list[0])
    y = int(list[1])
    h = list[2]
    cs = list[3]
    for c in cs:
        match c:
            case "A":
                match h:
                    case "N":
                        y += 1
                    case "W":
                        x -= 1
                    case "S":
                        y -= 1
                    case "E":
                        x += 1
            case "L":
                if dirs.find(h)+1>=len(dirs):
                    h = dirs[0]
                else:
                    h = dirs[dirs.find(h)+1]
            case "R":
                h = dirs[dirs.find(h)-1]
    print(f"{x} {y} {h}")