import random

# Define the Person class to represent a general human
class Person :
    def __init__(self , name):
        self.name = name
        
# Define the Player class that inherits from Person
class Player(Person):
    def setTheme (self , theme):
        self.theme = theme

# Get the player names as input and store them in a list
listOfNames = input().split("-")
print(listOfNames)

# Initialize counters for themes A and B
themeA = 0
themeB = 0

# Create a list to store the Player objects
listOfPlayers = list()

# Loop through each player name to assign themes A or B randomly
for i in range(len(listOfNames)):
    x = random.randint(0,1)
    player = Player(listOfNames[i].strip())
    # Ensure there are 12 players in each team (A and B) as per the task requirement
    if themeB< 12 and themeA <12 :
        if x == 0 :
            player.setTheme("A")
        else :
            player.setTheme("B")
    # If one team already has 12 players, assign the rest to the other team
    elif len(themeB)< 12 :
        player.setTheme("B")
    else:
        player.setTheme("A")
    listOfPlayers.append(player)

# Print the names and themes of each player
for i in range(len(listOfNames)):
    print(listOfPlayers[i].name , " " , listOfPlayers[i].theme)

