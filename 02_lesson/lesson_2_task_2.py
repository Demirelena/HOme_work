def is_year_leap(year):
    return year % 4 == 0


year_to_check = 2057

result = is_year_leap(year_to_check)

print("год", year_to_check, ":", result)
