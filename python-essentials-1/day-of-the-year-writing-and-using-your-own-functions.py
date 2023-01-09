def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(year, month):
    if month < 1 and month > 12:
        return None
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_year_leap(year):
        return 29
    else:
        return 28


def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or days_in_month(year, month) < day or day < 1 or day > 31:
        return None
    days = day
    for i in range(1, month):
        days += days_in_month(year, i)
    return days


print(day_of_year(2000, 12, 31))
print(day_of_year(2022, 12, 19))
print(day_of_year(2022, 11, 1))
print(day_of_year(2000, 11, 31))
