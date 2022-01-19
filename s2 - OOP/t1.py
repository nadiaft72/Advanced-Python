import statistics

class Students:
    count = 0
    def __init__(self , sen , ghad , vazn , count):
        self.sen = sen
        self.ghad = ghad
        self.vazn = vazn
        Students.count = count
    def aveOfSen(self):
        return(statistics.mean(self.sen))
    def aveOfGhad(self):
        return(statistics.mean(self.ghad))

    def aveOfVazn(self):
        return(statistics.mean(self.vazn))

    

n = input()    
listOfSen =input().split()
listOfGhad =input().split()
listOfVazn =input().split()
listOfSen= list(map(int , listOfSen))
listOfVazn= list(map(int , listOfVazn))
listOfGhad= list(map(int , listOfGhad))

studentsA = Students(listOfSen,listOfGhad,listOfVazn,n)


n = input()    
listOfSen =input().split()
listOfGhad =input().split()
listOfVazn =input().split()
listOfSen= list(map(int , listOfSen))
listOfVazn= list(map(int , listOfVazn))
listOfGhad= list(map(int , listOfGhad))

studentsB = Students(listOfSen,listOfGhad,listOfVazn,n)


aveOfSenA =studentsA.aveOfSen()
aveOfGhadA = studentsA.aveOfGhad()
aveOfVaznA = studentsA.aveOfVazn()
aveOfSenB = studentsB.aveOfSen()
aveOfGhadB = studentsB.aveOfGhad()
aveOfVaznB = studentsB.aveOfVazn()

print(float(aveOfSenA))
print(float(aveOfGhadA))
print(float(aveOfVaznA))
print(float(aveOfSenB))
print(float(aveOfGhadB))
print(float(aveOfVaznB))
string = "Same"
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

print(string)