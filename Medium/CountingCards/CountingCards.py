
cases = int(input())
for caseNum in range(cases):
    playerCards = input().split(" ")
    playerValue = 0
    for p in playerCards:
        value = p[:p.find("_")]
        try:
            int(value)
            playerValue += int(value)
        except ValueError:
            if value=="KING" or value=="QUEEN" or value=="JACK":
                playerValue += 10
            elif value=="ACE":
                if playerValue >= 11:
                    playerValue += 1
                else:
                    playerValue += 11
    computerCards = input().split(" ")
    computerValue = 0
    for c in computerCards:
        value = c[:c.find("_")]
        try:
            int(value)
            computerValue += int(value)
        except ValueError:
            if value in ["KING", "QUEEN", "JACK"]:
                computerValue += 10
            elif value == "ACE":
                if computerValue >= 11:
                    computerValue += 1
                else:
                    computerValue += 11
    if playerValue > 21:
        status = "Dealer Wins"
    elif computerValue > 21 and playerValue <= 21:
        status = "Player Wins"
    elif (21 - playerValue) < (21 - computerValue):
        status = "Player Wins"
    elif (21 - playerValue) > (21 - computerValue):
        status = "Dealer Wins"
    elif (21 - playerValue) == (21 - computerValue):
        status = "Tie"
    print(f"Player Score: {playerValue} Dealer Score: {computerValue} {status}!")