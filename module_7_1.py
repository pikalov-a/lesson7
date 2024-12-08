##"Режимы открытия файлов"#module_7_1.py
##Задача "Учёт товаров":
#from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        def __str__(self):
            xpri =self.name +', '+str(self.weight)+', '+self.category
            return xpri
#            return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self, _file_name = 'products.txt'):
        self._file_name=_file_name
    def get_products(self):
        file= open(self._file_name,'r')
        string=file.read()
        file.close()
        return string
    def add(self, *products):
#        xproducts=(f'{products[0].name}, {products[0].weight}, {products[0].category}')
        print(products[0])
#        self.products=products
        xproducts=str(products[0])
#        print(self.products)
        self.string=self.get_products()
        for i in range(len(products)):
#            if self.products[i] not in self.string:
                file=open(self._file_name, 'a')
                file.write(str(products[i]))
                file.write('/n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

###в ADD мы передаем кортеж из 3 кортежей
### он раскручивается ниже НО в реальности так не получается.  В ЧЕМ ПРОБЛЕМА?
#p1=('Spaghetti', 3.4, 'Groceries')
#p2=('Potato', 50.5, 'Vegetables')
#p3=('Spaghetti', 3.4, 'Groceries')
#def add( *products):
#    print(products)
#    print(products[0][0])
#    print(products[0][1])
#    print(products[0][2])
#
#xadd=add(p1,p2,p3)
