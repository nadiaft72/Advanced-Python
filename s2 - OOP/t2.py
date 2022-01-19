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