def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = 2024
print(f"Is {year} a leap year? {is_leap_year(year)}.")
