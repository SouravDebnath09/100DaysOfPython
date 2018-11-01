# This is to find the day of any date
import datetime
# This is how you need to call your own function
import DiffInDaysFunc

days = ["Sunday","Monday","Tuesday","Wednesday", "Thursday","Friday", "Saturday"]
defaultDate = datetime.date(2000,1,2)

DateYear = int(input("Enter the first date year:"))
DateMonth = int(input("Enter the first date month:"))
DateDay = int(input("Enter the first date day:"))

date = datetime.date(DateYear,DateMonth,DateDay)

Diff = DiffInDaysFunc.DifferenceInDays(date,defaultDate)

DaythOfDiff = Diff%7

print(" The day of the given " + str(date)+" is " + days[DaythOfDiff])