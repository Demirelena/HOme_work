def is_year_leap(year):
    return year % 4 == 0

# Выбираем любой год для проверки
year_to_check = 2057  # можно изменить на любой другой год

# Сохраняем результат вызова функции в переменную
result = is_year_leap(year_to_check)

# Выводим результат
print("год", year_to_check, ":", result)

