import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    year = int(sys.stdin.readline().rstrip())
    aspect = "Yang" if year%2==0 else "Yin"
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    element = elements[((year-4)%10)//2]
    animals =  ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    animal = animals[(year-4)%12]
    print(f"{year} {aspect} {element} {animal}")

