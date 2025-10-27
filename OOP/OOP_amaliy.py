# class Book:
#     def __init__(self , kitob_nomi  , avtori , yili):
#         self.kitob_nomi = kitob_nomi
#         self.avtori = avtori
#         self.yili = yili
#     def malumot(self):
#         return f'{self.avtori}ning kitobi {self.kitob_nomi} va {self.yili}yilda chop etilgan'
# class Dokon:
#     def __init__(self, dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.kitoblar = []
#     def add_book(self ,kitob_nomi  , avtori , yili):
#         books = Book(kitob_nomi  , avtori , yili)
#         self.kitoblar.append(books)
#     def get_info(self):
#         book = "\n".join([kitob.malumot() for kitob in self.kitoblar])
#         return f'{self.dokon_nomi} dokonida mavjud bolgan kitoblar:\n{book}'
    
# dokon1 = Dokon('Brnasa')
# dokon1.add_book('Dollarlik muaffaqiyat' , 'Silvester Stollone' , 2009)
# dokon1.add_book('Davinchi siri' , ' Den Braun' , 2003)
# print(dokon1.get_info())


class Book:
    def __init__(self , book_name  , book_author , book_year):
        self.name = book_name
        self.author = book_author
        self.year = book_year
        self_yoqimlilar = []
        
    def get_info(self):
         return f'Kitob nomi: {self.book_name} \nKitob yozuvchisi {self.author}  \nKitob chop etilgan yil{self.year}'
    def get_year(self,yil):
        self.yil = yil
        return f'Kitob yozilganiga {self.yil - self.year}yil boldi'
    def add_favorite(self):
        self.yoqimlilar.append(self.name)
        return f'Menga yoqgan kitob {self.yoqimlilar} va u haqida malumot {self.get_info()}'
        