##"Позиционирование в файле"#module_7_2.py
##Задача "Записать и запомнить":
def custom_write(file_name, strings):
    strings_positions={}
    file = open(file_name, 'a', encoding='utf-8')
    xn=file.tell()
    for i in range(len(strings)):
        strings_positions[(i+1,file.tell())]=strings[i]
        file.write(strings[i])
        file.write('\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
