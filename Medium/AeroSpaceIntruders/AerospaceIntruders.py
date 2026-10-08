
cases = int(input())
for caseNum in range(cases):
    speed = {"A":10, "B":20, "C":30}
    ships: dict[str, list] = {}
    targets = {}
    sh = int(input())
    for s in range(sh):
        ship = input()
        ships[ship.split("_")[0]] = [ship.split("_")[1][:1], int(ship.split(":")[1].split(",")[0]), int(ship.split(":")[1].split(",")[1])]
    for i in range(len(ships)):
        closest = ""
        for n, v in ships.items():
            if closest not in ships.keys() or v[1]-speed[v[0]] < ships[closest][1]-speed[ships[closest][0]]:
                closest = n
            elif v[1]-speed[v[0]] == ships[closest][1]-speed[ships[closest][0]] and v[2]>ships[closest][2]:
                closest = n
            print(closest)

        targets[closest] = ships[closest][1]

        for n, v in ships.items():
            ships[closest][1] -= speed[ships[closest][0]]
    for k, v in targets.items():
        print(f"Destroyed Ship: {k} xLoc: {v}")