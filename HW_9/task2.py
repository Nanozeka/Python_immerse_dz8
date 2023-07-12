# Задача 2
# Напишите следующие функции:
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.


import csv
from random import randint

def generate_csv_file(filename, num_rows):
    """
    Генерирует CSV-файл с указанным именем, содержащий случайные числа в каждой строке.
    В файле будет указано заданное количество строк.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [randint(1, 1000), randint(1, 1000), randint(1, 1000)]
            writer.writerow(row)


if __name__ == '__main__':
    filename = "random_numbers.csv"
    num_rows = 200
    generate_csv_file(filename, num_rows)
    print(f"Файл {filename} успешно создан с {num_rows} строками случайных чисел.")