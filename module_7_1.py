##"Режимы открытия файлов"#module_7_.py
##Задача "Учёт товаров":
#from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name=name
        self.weight=weight
        self.category=category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name=__file_name
    def get_products(self):
        file= open(self.__file_name,'r')
        string=file.read()
        file.close()
        return string
    def add(self, *products):
        self.string=self.get_products()
        for i in range(len(products)):
            xpri = str(products[i])
            xpri1 = xpri[0:xpri.find(",")]
            if str(products[i]) not in self.string:
                file=open(self.__file_name, 'a')
                file.write(xpri)
                file.write('\n')
                file.close()
            else:
                print(f'Продукт {xpri1} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
