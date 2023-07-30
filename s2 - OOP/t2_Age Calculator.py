from datetime import datetime # Current date time in local system  # Import necessary modules from the datetime library
from datetime import date  # Import the date class

#print(datetime.now())

birthDate = input()  # Get the birthdate as input from the user
if birthDate[4] == "/" and birthDate[7]=="/":    # Validate the input date format
    #print(birthDate[0:4] , " ", birthDate[5:7]," ", birthDate[8:0])
    yy = int(birthDate[0:4])  # Extract the year from the input
    mm = int(birthDate[5:7])  # Extract the month from the input
    dd = int(birthDate[8:])  # Extract the day from the input

    # Check if the date components are valid (year > 0, month between 1 and 12, day between 1 and 31)
    if yy > 0 and mm > 0 and mm < 13 and dd > 0 and dd < 32:
        today = date.today()  # Get the current date
        age = today.year - yy - ((today.month, today.day) < (mm, dd))  # Calculate the age
        print(age)  # Print the calculated age
    else:
        print("WRONG")  # Print "WRONG" if the date components are invalid
else:
    print("WRONG")  # Print "WRONG" if the date format is incorrect
