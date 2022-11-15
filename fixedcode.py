import random

#mild
def candyrandom():
    x  = random.randrange(0, 100)
    y = random.randrange(1,5)
    if x < 15:
        print("you got", y, " Butterfingers")
        candy[0] += y
    elif x < 35:
        print("you got", y, " Hershey's")
        candy[1] += y
    elif x < 70:
        print("you got", y, " Peanut  buttercups")
        candy[2] += y
    elif x < 80:
        print("you got", y, " M&Ms")
        candy[3] += y
    elif x < 98:
        print("you got", y, "Sour Patch Kids")
        candy[4] += y
    else:
        print("you got a rock")
        y = 1
        candy[5] += y
        
candy = [0,0,0,0,0,0]

candyrandom()
candyrandom()
candyrandom()
candyrandom()
candyrandom()

print("final candy count for each kid:", candy)


#medium

class Fridge:
    def __init__(self):
        self.NumberOfItems = 0
        self.DoorOpen = False
        self.isRunning = True
        
    def printfunc(self, z):
        if z == 'a':
            print("There are,", self.NumberOfItems, " items in the fridge")
            print("Fridge Open is:", self.DoorOpen)
            print("The Fridge running is:", self.isRunning)
            if self.isRunning == True:
                print("Haha your fridge is running, better go catch it!")
        if z == 'i':
            print("There are,", self.NumberOfItems, " items in the fridge")
        if z == 'd':
            print("Fridge Open is:", self.DoorOpen)
        if z == 'r':
            print("The Fridge running is:", self.isRunning)
            if self.isRunning == True:
                print("Haha your fridge is running, better go catch it!")
                
    def openDoor(self):
        self.DoorOpen = True
    def closeDoor(self):
        self.DoorOpen = False
    def fillFridge(self, x):
        if self.DoorOpen == True:
            self.NumberOfItems += x
        else:
            print("error")
    def MakeDinner(self):
        if self.DoorOpen == True:
            self.NumberOfItems -= 10
        else:
            print("You can't make dinner the door is closed")

print()
fridge = Fridge()

fridge.printfunc('a')
print()
fridge.openDoor()
fridge.printfunc('d')

y = int(input("How many items do you want to put in the fridge?"))
fridge.fillFridge(y)
fridge.printfunc('i')
choice = input("Do you want to make dinner?")
if choice == "yes":
    fridge.MakeDinner()
else:
    print("ok, dinner wasn't made")
    
print("Now", end = ' ')
fridge.printfunc('i')

lol= input("close the fridge door?")
if lol == "yes":
    fridge.closeDoor()
else:
    fridge.openDoor()

fridge.printfunc('d')

