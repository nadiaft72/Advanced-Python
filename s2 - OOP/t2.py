'''Write a program that uses the datetime library class in Python to calculate the age of a person.
If the input date is incorrect, print the word "WRONG" in the output. The date format should be yyyy/mm/dd.
For example, if someone enters 15 for the month, it should print "WRONG" because we only have 12 months.
The same applies to the number of days, which should not exceed 31.

Note: The sample input and output below correspond to running the program on the date 2019/02/01.

Sample Input:
1995/02/03

Sample Output:
24'''

from datetime import datetime # Current date time in local system 
from datetime import date

#print(datetime.now())

birthDate = input()
if birthDate[4] == "/" and birthDate[7]=="/":
    #print(birthDate[0:4] , " ", birthDate[5:7]," ", birthDate[8:0])
    yy = int(birthDate[0:4])
    mm = int(birthDate[5:7])
    dd = int(birthDate[8:])
    if yy>0 and mm>0 and mm < 13 and dd>0 and dd<32:
        today = date.today()
        age = today.year - yy - ((today.month, today.day) < (mm, dd))
        print(age)
    else:
        print("WRONG ")

else:
    print("WRONG ")        
