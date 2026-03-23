#Calendar Display Program in Python
import calendar
from py_compile import main
def display_calendar(year, month):
    print(calendar.month(year, month))

display_calendar(2023, 10)
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
display_calendar(year, month)

print("Calendar Display Program")
input("Press Enter to display the calendar...")