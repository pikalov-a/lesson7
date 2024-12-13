##"Файлы в операционной системе"#module_7_5.py
##имеются ошибки при при печати информации обычных файлов, закономерности не выявил
##для отсутвия ошибок их скорее всего надо ловить 
import os.path
import time
#directory = "C:\install"
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file)

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

