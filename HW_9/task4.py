# Задача 4
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json


def save_quadratic_equation_results_to_json(func):
    def wrapper(a, b, c):
        # Создание словаря с переданными параметрами
        equation_info = {
            "a": a,
            "b": b,
            "c": c
        }

        # Выполнение функции для получения результатов
        results = func(a, b, c)

        # Добавление результатов в словарь
        equation_info["results"] = results

        # Загрузка данных в JSON файл
        with open("quadratic_equation_results.json", "a") as file:
            json.dump(equation_info, file)
            file.write('\n')  # Добавляем перенос строки между записями

    return wrapper

@save_quadratic_equation_results_to_json
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return [x1, x2]


if __name__ == '__main__':
    with open("random_numbers.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                params = list(map(int, row))
                solve_quadratic_equation(*params)
            else:
                print("Некорректная тройка чисел в файле.")

    print("Результаты сохранены в quadratic_equation_results.json")