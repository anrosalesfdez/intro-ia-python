
import calendar

#
# 4.3.1.7 LAB: How many days: writing and using your own functions
#
def days_in_month(year: int, month: int) -> int:
    """Return the number of days in a given month and year."""
    if year < 1 or year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    return calendar.monthrange(year, month)[1]

print(days_in_month(2024, 2))
#print(days_in_month(2024, 13))

v_year = int(input('Enter a year:'))
v_month = int(input('Enter a month:'))
print(days_in_month(v_year, v_month))
