import statistics

# Define the Students class
class Students:
    count = 0

    # Constructor to initialize student attributes
    def __init__(self , sen , ghad , vazn , count):
        self.sen = sen
        self.ghad = ghad
        self.vazn = vazn
        Students.count = count
    
    # Calculate the average age of students
    def aveOfSen(self):
        return(statistics.mean(self.sen))

    # Calculate the average height of students
    def aveOfGhad(self):
        return(statistics.mean(self.ghad))

    # Calculate the average weight of students
    def aveOfVazn(self):
        return(statistics.mean(self.vazn))

    
# Input and process data for students of class A
n = input()    
listOfSen =input().split()
listOfGhad =input().split()
listOfVazn =input().split()
listOfSen= list(map(int , listOfSen))
listOfVazn= list(map(int , listOfVazn))
listOfGhad= list(map(int , listOfGhad))
studentsA = Students(listOfSen,listOfGhad,listOfVazn,n)

# Input and process data for students of class B
n = input()    
listOfSen =input().split()
listOfGhad =input().split()
listOfVazn =input().split()
listOfSen= list(map(int , listOfSen))
listOfVazn= list(map(int , listOfVazn))
listOfGhad= list(map(int , listOfGhad))
studentsB = Students(listOfSen,listOfGhad,listOfVazn,n)

# Calculate and print the average age, height, and weight for class A
aveOfSenA =studentsA.aveOfSen()
aveOfGhadA = studentsA.aveOfGhad()
aveOfVaznA = studentsA.aveOfVazn()
print(float(aveOfSenA))
print(float(aveOfGhadA))
print(float(aveOfVaznA))

# Calculate and print the average age, height, and weight for class B
aveOfSenB = studentsB.aveOfSen()
aveOfGhadB = studentsB.aveOfGhad()
aveOfVaznB = studentsB.aveOfVazn()
print(float(aveOfSenB))
print(float(aveOfGhadB))
print(float(aveOfVaznB))
string = "Same"

# Compare average heights and weights of both classes to determine the class with the highest average height
if aveOfGhadA!=aveOfGhadB:
    if aveOfGhadB < aveOfGhadA :
        string = "A"
    else:
        string="B"
elif aveOfVaznA!= aveOfVaznB : 
    if aveOfVaznB > aveOfVaznA :
        string = "A"
    else:
        string = "B"
        
# Print the result indicating the class with the highest average height or "Same" if both are equal
print(string)
