import random
class Person :
    def __init__(self , name):
        self.name = name

class Player(Person):
    def setTheme (self , theme):
        self.theme = theme

listOfNames = input().split("-")
print(listOfNames)
themeA = 0
themeB = 0
listOfPlayers = list()
for i in range(len(listOfNames)):
    x = random.randint(0,1)
    player = Player(listOfNames[i].strip())
    if themeB< 12 and themeA <12 :
        if x == 0 :
            player.setTheme("A")
        else :
            player.setTheme("B")
    elif len(themeB)< 12 :
        player.setTheme("B")
    else:
        player.setTheme("A")
    listOfPlayers.append(player)

for i in range(len(listOfNames)):
    print(listOfPlayers[i].name , " " , listOfPlayers[i].theme)

