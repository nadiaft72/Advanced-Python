'''In schools A and B, two different health programs have been considered.
In one school, milk is distributed, while in the other school it is not. Nutrition experts intend to compare these two classes by examining the height, weight, and age of the students.
Write a program that takes the number of students in each class, along with their age, height, and weight, and stores them in separate lists. 
Then, print the average age, height, and weight of each class on separate lines (printed as floats). Finally, print the class with the highest average height.
If the average heights are equal, print the class with the lower average weight. If both the average height and weight are equal, print "Same" exactly as written.
Using a class in solving this exercise is necessary.

input :
5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47

output :
16.2
172.4
63.0
15.8
164.4
51.6
A

'''


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
