import random


classmates = ["Alex", "Jacob", "Tam", "Jesse", "Ricardo", "Lukas", "Kevin", "Simon", "Rey", "Lalo"]
locations = ["the Cafeteria", "Room 110", "the Library", "Automotive", "Welding"]

def Clue():
    victim = random.randrange(0, 10)
    place = random.randrange(0, 5)
    attacker = random.randrange(0, 10)
    attack = random.randrange(0, 100)
    
    if attack < 10:
        print(classmates[victim], "was water ballooned in", locations[place], "by,", classmates[attacker])
    elif attack < 30:
        print(classmates[victim], "was pied in the face in", locations[place], "by,", classmates[attacker])
    elif attack < 65:
        print(classmates[victim], "was given chocolate chips cookies that were actually oatmeal raisin cookies in", locations[place], "by,", classmates[attacker])
    elif attack < 80:
        print(classmates[victim], "had their shoelaces tied together in", locations[place], "by,", classmates[attacker])
    else:
        print(classmates[victim], "was transformed into a rabbit with a transfiguration raygun in", locations[place], "by,", classmates[attacker])
        
x = 0
while x <= 10:
    Clue()
    print()
    x += 1
