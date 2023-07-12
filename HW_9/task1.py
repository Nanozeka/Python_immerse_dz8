# Задача 1
# Напишите следующие функции:
# Нахождение корней квадратного уравнения

def solve_quadratic_equation(a, b, c):
    """
    Находит корни квадратного уравнения ax^2 + bx + c = 0.
    Возвращает список корней или None, если корней нет.
    """
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

    a = 1
    b = -3
    c = 2
    roots = solve_quadratic_equation(a, b, c)
    if roots:
        print("Корни квадратного уравнения:", roots)
    else:
        print("Квадратное уравнение не имеет корней.")