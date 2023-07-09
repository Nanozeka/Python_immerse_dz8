import os
import json
import csv
import pickle

__all__ = ["traverse_directory"]

def traverse_directory(directory):
    result = []

    # Делаем рекурсивный обход директорий
    for root, dirs, files in os.walk(directory):
        current_dir_size = 0  # Размер текущей директории

        for file in files:

            # Создаем путь к текущему файлу, объединяя текущий каталог и имя файла.
            file_path = os.path.join(root, file)

            # Получаем размер файла в байтах
            file_size = os.path.getsize(file_path)

            #Увеличиваем размер текущей директории на размер текущего файла.
            current_dir_size += file_size

            # Добавляем информацию о текущем файле
            result.append({
                'type': 'file',
                'name': file,
                'parent_directory': root,
                'size': file_size
            })

        result.append({
            'type': 'directory',
            'name': os.path.basename(root),
            'parent_directory': os.path.dirname(root),
            'size': current_dir_size
        })

    # Записываем результаты в файлы JSON, CSV и pickle
    with open('result.json', 'w') as json_file:
        json.dump(result, json_file)

    with open('result.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['type', 'name', 'parent_directory', 'size'])
        writer.writeheader()
        writer.writerows(result)

    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)

if __name__ == '__main__':
    traverse_directory(".")