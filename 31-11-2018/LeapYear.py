# This is another simple code to find out the year is leap year or not
year = int(input("Please enter the year:"))
# Logic to check leap year

if(year%100==0):
    if(year%400==0):
        print("The "+ str(year) + " is leap year")
    else:
        print("The "+ str(year) + " is not leap year")
elif(year%4==0):
    print("The "+ str(year) + " is leap year")
else:
    print("The "+ str(year) + " is not leap year")