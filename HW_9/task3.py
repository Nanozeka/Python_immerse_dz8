# Задача 3
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

import csv

def run_quadratic_equation_on_csv(func):
    def wrapper(filename):
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    roots = func(a, b, c)
                    print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c} = 0: {roots}")
                else:
                    print("Некорректная тройка чисел в файле.")

    return wrapper


@run_quadratic_equation_on_csv
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
    solve_quadratic_equation("random_numbers.csv")