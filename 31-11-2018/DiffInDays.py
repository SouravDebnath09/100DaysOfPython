import  datetime

firstDateYear = int(input("Enter the first date year:"))
firstDateMonth = int(input("Enter the first date month:"))
firstDateDay = int(input("Enter the first date day:"))

firstdate = datetime.date(firstDateYear,firstDateMonth,firstDateDay)

SecondDateYear = int(input("Enter the second date year:"))
SecondDateMonth = int(input("Enter the second date month:"))
SecondDateDay = int(input("Enter the second date day:"))

SecondDate = datetime.date(SecondDateYear,SecondDateMonth,SecondDateDay)

differenceInDay = SecondDate - firstdate

print(differenceInDay.days)