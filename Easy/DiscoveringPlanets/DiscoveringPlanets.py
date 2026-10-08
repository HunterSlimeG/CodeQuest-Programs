
cases = int(input())
for caseNum in range(cases):
    temp, wtr, mag, orb = input().split(" ")
    temp = float(temp)
    wtr = True if wtr == "true" else False
    mag = True if mag == "true" else False
    orb = float(orb)

    if temp > 100:
        print("The planet is too hot.")
    elif temp < 0:
        print("The planet is too cold.")
    elif not wtr:
        print("The planet has no water.")
    elif not mag:
        print("The planet has no magnetic field.")
    elif orb > 0.6:
        print("The planet's orbit is not ideal.")
    else:
        print("The planet is habitable.")