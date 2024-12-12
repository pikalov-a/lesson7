##"Оператор "with""#module_7_3.py
##Задача "Найдёт везде":

import os
import string
#test_str = 'Gfg, is best: for ! Geeks ;'
#test_str = test_str.translate(str.maketrans('', '',string.punctuation))
#print(test_str)
class WordsFinder:
    def __init__(self, *files):
        self.files=files
        print(files)
        print(files[0])
#        all_words={}
#        file_names=[]
    def get_all_words(*files):
#!!!!надо как-то как Вы говорите пробросить или распаковать
#из *files надо сделать tupple не могу понять как
        all_words = {}
        file_names = []
        word=[]
        for i in range(len(files)):
##!!!возможная ошибка. Надо добавить в список файлов название файла
            file_names.append(files[i])   ## возможная ошибка
            print(files[i])
            with open(files[i]) as file:
                xword=file.read()
#                xword=xword.lower()
#                word[i] = xword.split()
                # punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                punc1 = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for ele in punc1:
                    if ele in xword:
                        xword= xword.replace(ele, "")
                xword=xword.lower()
            all_words[files[i]] = xword.split()
        def find(self, word):
            return self.index(word)
        def count(self, word):
            return self.count(word)

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
