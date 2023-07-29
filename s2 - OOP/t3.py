'''Write a program in which there is a football player class that inherits characteristics from the human class.

The program should start by creating 22 football player objects, and then assign the following player names to each object. 
Using the random method and inheritance, divide these 22 names between teams A and B, and finally print the name of each player along with the name of the team they belong to.

Player names:

Hossein - Maziar - Akbar - Nima - Mehdi - Farhad - Mohammad - Khashayar - Milad - Mostafa - Amin - Saeed - Pouya - Porya - Reza - Ali - Behzad - Soheil - Behrouz - Shahrouz - Saman - Mohsen
'''

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

