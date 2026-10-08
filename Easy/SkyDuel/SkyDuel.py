
cases = int(input())
for caseNum in range(cases):
    line = [int(i) for i in input().split(" ")]
    missions = line[0]
    raptor = line[1:5]
    raider = line[5:]
    for m in range(missions):
        mission = [int(i) for i in input().split(" ")]
        if (not raptor[2] > mission[1]) and raider[2] > mission[1]:
            print("Sikorsky Raider")
        elif (not raider[2] > mission[1]) and raptor[2] > mission[1]:
            print("F-22 Raptor")
        elif raptor[2] > mission[1] and raider[2] > mission[1]:
            raptorTime = (mission[0]/raptor[0])*360
            raptorFuel = mission[0]*raptor[1]
            raptorScore = raptorTime+raptorFuel+raptor[3]

            raiderTime = (mission[0]/raider[0])*360
            raiderFuel = mission[0]*raider[1]
            raiderScore = raiderTime+raiderFuel+raider[3]

            print(raptorScore)
            print(raiderScore)
            if raiderScore<raptorScore:
                print("Sikorsky Raider")
            else:
                print("F-22 Raptor")