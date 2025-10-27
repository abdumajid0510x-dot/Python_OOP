# class Talaba:
#     def __init__(self , ism , familiya , baho):
#         self.ism = ism
#         self.familiya = familiya
#         self.baho = baho
#     def bahola(self):
#         return self.baho
#     def natija(self):
#         if self.baho == 5:
#             return 'A\'lo'
#         elif self.baho == 4:
#             return 'Yaxshi'
#         elif self.baho == 3:
#             return 'Qoniqarli'
#         else:
#             return('Qoniqarsiz')




  


# talaba1 = Talaba('Ali' , 'Aliyev' , 5)
# print(talaba1.natija())


# class Dokon: 
#     def __init__(self , maxsulot , narx):
#         self.maxsulot = maxsulot
#         self.narx = narx
#     def chiqar(self):
#         return self.maxsulot , self.narx
# mahsulot1= Dokon('Non' , '3000')
# print(mahsulot1.chiqar())


# class Mashina: 
#     def __init__(self , brend , model , yil, ):
#         self.brend = brend
#         self.model = model
#         self.yili = yil
#         self.kraska = []
#     def haqida(self):
#         print(f"{self.brend} -mashina brendi , {self.model} - mashina modeli")
#     def ishlab_chiqarish(self):
#         if self.yili>2020:
#             return 'Zamonaviy'
#         elif 2020>self.yili>2000:
#             return 'Classic'
#         elif self.yili<2000:
#             return 'Retro'
#         else:
#             return 'Xatolik!!'
#     def kraskasi_haqida(self , kraska):
#         self.kraska.append(kraska)
#     def malumot_ber (self):
#         print(f'{self.kraska} - kraska holati')
# mashina1 = Mashina('Lambogini' , 'Urus' , 1999  )
# mashina1.kraskasi_haqida('Kraskasi toza')
# mashina2 = Mashina('Lambogini' , 'Aventador' , 2020 )
# mashina3 = Mashina('Bugatti' , 'Chiron' , 2016 )
# print(mashina1.haqida(),mashina1.ishlab_chiqarish(),mashina1.malumot_ber())
# print(mashina2.haqida(),mashina2.ishlab_chiqarish())
# print(mashina3.haqida(),mashinaf3.ishlab_chiqarish())



# class Mashina:
#     def __init__(self,madel,probeg,yil,rang):
#         self.madel = madel
#         self.probeg = probeg
#         self.yil = yil
#         self.rang =rang
#     def get_info(self):
#         return print(f'{self.madel} - modeli , {self.probeg} - yurgan , {self.yil} - yili , {self.rang} - rang')

# class Bozor:
#     def __init__(self,bozor):
#         self.bozor = bozor
#         self.mashinalar_soni = 0
#         self.royhat = []
#     def avto_qosh(self,madel,probeg,yili,rang):
#         mashina = Mashina(madel,probeg,yili,rang)
#         self.royhat.append(mashina)
#         self.mashinalar_soni+= 1
#     def avto_info(self):
        # car = " \n".join([avto.get_info() for avto in self.royhat])
#         return f'Bozorimizda {self.mashinalar_soni} ta moshina bor \n{car} \n'
    

# mashina = Bozor('GM avto')
# mashina.avto_qosh('Cobalt' , 34000 , 2022, 'Oq')
# mashina.avto_qosh('Gentra' , 40000 , 2023 , 'qora')

# print(mashina.avto_info())




# class maxsulot:
#     def __init__(self,maxsulot,kg_naxr):
#         self.madel = maxsulot
#         self.kg.naxr = kg_narx
#     def get_info(self):
#         return print(f'{self.madel} - modeli , {self.probeg} - yurgan )

# class Dokon:
#     def __init__(self,bozor):
#         self.bozor = bozor
#         self.mashinalar_soni = 0
#         self.royhat = []
#     def avto_qosh(self,madel,probeg,yili,rng):
#         mashina = Mashina(madel,probeg,yili,rang)
#         self.royhat.append(mashina)
#         self.mashinalar_soni+= 1
#     def avto_info(self):
#         car = " \n".join([avto.get_info() for avto in self.royhat])
#         return f'Bozorimizda {self.mashinalar_soni} ta moshina bor \n{car} \n'
    

# mashina = Bozor('GM avto')
# mashina.avto_qosh('Cobalt' , 34000 , 2022, 'Oq')
# mashina.avto_qosh('Gentra' , 40000 , 2023 , 'qora')

# print(mashina.avto_info())



# class Talaba:
#     def __init__(self, ismi , yoshi , kursi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.kursi = kursi
#     def yangilash(self):
#         self.kursi +=1
#         self.yoshi +=1
#     def end_uni(self):
#         bitirganmi = False
#         if self.kursi == 4:
#             bitirganmi = True
#             return 'Bitiruvchi talaba'
#         else:
#             return 'Hali oqiydi'
#     def about(self):
#         return f'Talaba: ismi {self.ismi} yoshi {self.yoshi}da va {self.kursi}-kursda oqiydi'
# talaba1 = Talaba('Ali', 18 , 1)
# talaba1.yangilash()
# talaba1.yangilash()
# print(talaba1.about())
# print(talaba1.end_uni())


# class Dokon:
#     def __init__(self, turi, narxi ):
#         self.turi = turi
#         self.narxi = narxi
#     def update(self , yangi_narx , yangi_nom):
#         self.yangi = yangi_narx
#         self.yangi_nom = yangi_nom
#     def about(self):
#         yangilash = False
#         if self.narxi == 25000:
#             yangilash = True
#             return 'Yangilash tugadi'
#         else:
#             return 'Hali yangilanadi'
#     def mahsulot(self):
#         return f'Maxsulot turi {self.turi} va narxi {self.narxi}'
# maxsulot1= Dokon(yangi_nom , 18000)
# yangi_nom = input('Yangi maxsuloti kiriting')
# yangi_narx = int(input('Yangi narxni kiriting: '))
# maxsulot1.update(yangi_narx)
# print(maxsulot1.mahsulot(), maxsulot1.about())



# class Dokon:
#     def __init__(self, turi, narxi):
#         self.turi = turi
#         self.narxi = narxi
#         self.mahsulotlar_royhati = []
#     def update(self, yangi_narx, yangi_nom):
#         self.narxi = yangi_narx
#         self.turi = yangi_nom
#         self.mahsulotlar.append(mahsulotlar_royhati)
#     def mahsulot(self):
#         return f'Maxsulot turi {self.turi} va narxi {self.narxi}som'


# yangi_nom = input('Yangi maxsulotni kiriting: ')
# yangi_narx = int(input('Yangi mmaxsulotning narxni kiriting: '))
# maxsulot1 = Dokon("", 18000)
# maxsulot1.update(yangi_narx, yangi_nom)

# print(maxsulot1.mahsulot())




# class Talaba:
#     def __init__(self , ismi , sinfi ):
#         self.ismi = ismi
#         self.sinfi = sinfi
#     def get_talaba_info(self):
#         return f'Talaba ismi: {self.ismi} , Talaba sinfi: {self.sinfi}'

# class Maktab:
#     def __init__(self, maktab_nomi , sinflar):
#         self.maktab_nomi = maktab_nomi
#         self.sinflar = sinflar
#         self.talaba_soni = 0
#         self.talabalar = []
#     def add_students(self , ismi , sinfi):
#         self.sinfi = sinfi
#         students = Talaba(ismi , sinfi)
#         self.talabalar.append(students)
#         self.talaba_soni +=1
#     def malumot_ber(self):
#         students = "\n".join([tolib.get_talaba_info() for tolib in self.talabalar ])
#         return f'{self.maktab_nomi}-maktabda {self.sinflar}-sinfida talim oluvchi \n{students}'
    
# maktab1 = Maktab('Sizov' , 8)
# maktab1.add_students('Abdumajid' , 8)
# maktab1.add_students('Abduvaid' , 8)

# print(maktab1.malumot_ber())




# class Kompyuter:
#     def __init__(self , brend , narxi):
#         self.brend = brend
#         self.narxi = narxi
#     def malumot(self):
#         return f'Kompyuter brend: {self.brend} , va uning narxi: {self.narxi}$'
# class Dokon:
#     def __init__(self , dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.komplar = []
#     def kompqosh(self , brendi , narxi):
#         self.brendi = brendi
#         self.narxi = narxi
#         kompyuterlar = Kompyuter(brendi , narxi)
#         self.komplar.append(kompyuterlar)
#     def get_info(self):
#         students = "\n".join([pc.malumot() for pc in self.komplar])
#         return f'{self.dokon_nomi} dokonidagi kompyuterlar {self.komplar}'

# dokon1 = Dokon('IBM')
# dokon1.kompqosh('Lenovo' , 600)
# # dokon1.kompqosh('hp' , 700 )

# print(dokon1.get_info())




ism = input('Ism kiriting: ')
yangi = set(ism) 
print(len(yangi))