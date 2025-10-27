                    # 1
# class Talaba:
#     def __init__(self , ism  , kurs):
#         self.ism = ism
#         self.kurs = kurs
#     def get_info(self):
#         return f'Talaba ismi: {self.ism} va uning kursi {self.kurs}da'
# talaba1 = Talaba('Ali' ,  3)
# print(talaba1.get_info())


                # 2
# class Mashina: 
#     def __init__(self , brend , model , yil, ):
#         self.brend = brend
#         self.model = model
#         self.yili = yil
#     def haqida(self):
#         print(f"{self.brend} -mashina brendi , {self.model} - mashina modeli , va {self.yili}da ishlab chiqarlingan")
# mashina1 = Mashina('Lambogini' , 'Urus' , 2019  )
# print(mashina1.haqida())

                # 4
# class Hisoblash:
#     def __init__(self , son1 , son2):
#         self.son1 = son1
#         self.son2 = son2
#     def ayirish(self):
#         return f'{self.son1 - self.son2}'
#     def qoshish(self):
#         return f'{self.son1 + self.son2}'
#     def bolish(self):
#         return f'{self.son1 / self.son2}'
#     def kopaytirish(self):
#         return f'{self.son1 * self.son2}'
# hisobla = Hisoblash(6 , 5)
# print(hisobla.kopaytirish())


                    # 5
# class Talaba:
#     def __init__(self, ismi, familiyasi , baho):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.baho = baho
#     def update(self , yangi_baho):
#         self.yangi_baho = yangi_baho
#         self.baho = yangi_baho
#     def end_ball(self):
#         if self.baho > 5:
#             return 'Maximal ball 5ga teng'
#     def get_info(self):
#         return f'Talaba {self.ismi} {self.familiyasi} va uning bahosi {self.baho}'
# talaba1 = Talaba('Ali' , 'Aliyev' , 3)
# talaba1.update(6)
# talaba1.end_ball()
# print(talaba1.get_info())

# class Ishchi:
#     def __init__(self , ismi ,  stavka , soat):
#         self.ismi=  ismi
#         self.stavka = stavka
#         self.soat = soat
#     def get_info(self):
#         return f'Ishchi ismi {self.ismi} va uning oylig maoshi {self.stavka * self.soat}'
# ishchi1 = Ishchi('Ali' , 20.000 , 250)
# print(ishchi1.get_info())


                    # 7
# class Den:
#     def __init__(self , ismi ,  stavka , soat):
#         self.ismi=  ismi
#         self.stavka = stavka
#         self.soat = soat
#     def get_info(self):
#         return f'Ishchi ismi {self.ismi} va uning oylig maoshi {self.stavka * self.soat}so\'m'
    
# class Noch:
#     def __init__(self , ismi ,  stavka , soat):
#         self.ismi=  ismi
#         self.stavka = stavka
#         self.soat = soat
#     def get_info(self):
#         return f'Ishchi ismi {self.ismi} va uning oylig maoshi {self.stavka * self.soat}so\'m'
    
# ishchi1 = Den('Ali' , 30000 , 180 )
# print('Kunduzki smen ishchi: ' ,  ishchi1.get_info())
# ishchi2 = Noch('Doniyor' , 40000, 180)
# print('Kechki smen ishchi: ' , ishchi2.get_info())

# class Bhsob:
#     def __init__(self , pul):
#         self.pul = pul
#     def add_money(self , yangi):
#         self.yangi = yangi
#         self.pul = self.yangi
    