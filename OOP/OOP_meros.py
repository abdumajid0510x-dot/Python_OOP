# class Avto:
#     def __init__(self , madel , yil):
#         self.madel = madel
#         self.yil = yil
#     def get_info(self):
#         return f'Madel {self.madel} , va mashina yili {self.yil} '

# class Mashina(Avto):
#     def __init__(self, madel, yil , rang , probeg):
#         super().__init__(madel, yil)
#         self.rang = rang
#         self.probeg = probeg

#     def info(self):
#         return f'Madel {self.madel} , va mashina yili {self.yil} , mashiina rangi {self.rang} va {self.probeg}km yurgan '
    
# car = Mashina('Kia' , 2024 , "Qora" , 30000)
# print(car.info())




                                                                                                        # 1
# class Avto:
#     def __init__(self , brend , model):
#         self.brend = brend
#         self.model = model
#     def get_info(self):
#         return f'Brend {self.brend} , {self.model}'
    
# class Mashina(Avto):
#     def __init__(self, brend, model ,  yil , rang, probeg):
#         super().__init__(brend, model)  
#         self.yil = yil  
#         self.rang = rang
#         self.probeg = probeg
#     def info(self):
#         return f'Model {self.brend} {self.model} , {self.yil}yil ishlab chiqarlingan , rangi {self.rang} , {self.probeg}km yurgan'
    
# avto1 = Mashina('Mersedes' , 'G63', 2021 , 'qora'  , 34000)
# print(avto1.info())


                                                                                        # 2
# class Bola:
#     def __init__(self , ism  , yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def info(self):
#         return f'{self.ism} , yoshi {self.yosh}da'
    
# class Boy(Bola):
#     def __init__(self, ism, yosh , maktab):
#         super().__init__(ism, yosh)
#         self.maktab = maktab
#     def get_info(self):
#         return f'{self.ism} , yoshi {self.yosh}da , {self.maktab} maktabida talim oladi'

# boy1 = Boy('Ali' , 10  , 'Sizov')
# print(boy1.get_info())


                                                                                # 3
# class Hayvon:
#     def __init__(self, turi):
#         self.turi = turi
#     def malumot(self):
#         return f'Hayvon turi: {self.turi}'

# class Mushuk(Hayvon):
#     def __init__(self, turi , ovoz):
#         super().__init__(turi)
#         self.ovoz = ovoz 
#     def info(self):
#         return f'Hayvon turi: {self.turi} , {self.ovoz} dugan ovoz chiqaradi'
    
# class It(Hayvon):
#     def __init__(self, turi , voise):
#         super().__init__(turi)
#         self.voise = voise
#     def info(self):
#         return f'Hayvon turi: {self.turi} , {self.voise} dugan ovoz chiqaradi'
    

# hayvon1 = Mushuk('Mushuk' , 'Myau')
# hayvon2 = It('It' , 'Vouv')
# print(hayvon1.info())
# print(hayvon2.info())

                                                                    # 4
# class Avto:
#     def __init__(self , brend , model , rang):
#         self.brend = brend
#         self.model=  model
#         self.rang= rang
#     def info(self):
#         return f'{self.brend} {self.model} , {self.rang} rangli'

# class Bola(Avto):
#     def __init__(self, brend, model, rang , ismi , yoshi):
#         super().__init__(brend, model, rang)
#         self.ism = ismi
#         self.yoshi = yoshi
#     def get_info(self):
#         return f'{self.ism} , yoshi {self.yoshi}da. Harid qilmoqchi bolgan avtomobili: {self.info()}'

# bola1 = Bola('Mersedes', 'E63' , 'Seriy' , 'Aziz' , '29')
# print(bola1.get_info())


                                                                    # 5
# class Talaba:
#     def __init__(self , ism , fakultet , ):
#         self.ism = ism
#         self.fakultet = fakultet
#     def malumot(self):
#         return f'{self.ism} , {self.fakultet} fakulteti'
    
# class Bakalavr(Talaba):
#     def __init__(self, ism, fakultet , kursi , diplom):
#         super().__init__(ism, fakultet)
#         self.kursi = kursi
#         self.diplom = diplom
#     def info(self):
#         return f'{self.malumot()} , {self.kursi}-kursda talim oladi , {self.diplom} diplomiga oqiyabti'
    
# class Magister(Talaba):
#     def __init__(self, ism, fakultet , kurs , diplom):
#         super().__init__(ism, fakultet)
#         self.kurs = kurs
#         self.diplom = diplom
#     def get_info(self):
#         return f'{self.malumot()} , {self.kurs}-kursda talim oladi , {self.diplom} diplomiga oqiyabti'
    
# talaba1 = Bakalavr('Aziz' , 'Filologiya' , 2  , 'Bakalavr')
# talaba2 = Magister('Ali' , 'Iqsodiyot' , 1 , 'Magister')
# print(talaba1.info())
# print(talaba2.get_info())

                                                                # 6
# class Ustoz:
#     def __init__(self , ism , familiya):
#         self.ism = ism
#         self.familiya=  familiya
#     def malumot(self):
#         return f'{self.familiya} , {self.ism}'

# class Informatika_Ustoz(Ustoz):
#     def __init__(self, ism, familiya , yoshi , fani):
#         super().__init__(ism, familiya)
#         self.yoshi = yoshi
#         self.fani = fani
#     def get_info(self):
#         return f'{self.malumot()} , yoshi {self.yoshi}da , {self.fani} fanidan dars beradi'
        
# ustoz1 = Informatika_Ustoz('Ali', 'Aliyev' , 26 , 'Informatika')
# print(ustoz1.get_info())


                                                                                # 7
# class Texnika:
#     def __init__(self , turi , brend , narx ):
#         self.turi = turi
#         self.brend = brend
#         self.narx = narx
#     def malumot(self):
#         return f'Texnika turi: {self.turi}  , {self.brend} , {self.narx}$ '

# class Kompyuter(Texnika):
#     def __init__(self, turi, brend, narx , model):
#         super().__init__(turi, brend, narx)
#         self.model = model
#     def get_info(self):
#         return f'Texnika turi: {self.turi}\n{self.brend} {self.model}, narxi {self.narx}$ '
    
# texnika1 = Kompyuter('Kompyuter' , 'Apple' ,1200 , 'MacBook Air')
# print(texnika1.get_info())

                                                                                # 8
# class Mahsulot:
#     def __init__(self , turi , narxi):
#         self.turi = turi
#         self.narxi = narxi
#     def malumot(self):
#         return f'Mahsulot turi: {self.turi}\n'
    
# class Telefon(Mahsulot):
#     def __init__(self, turi, narxi , brend , model , xotira):
#         super().__init__(turi, narxi)
#         self.brend = brend
#         self.model = model
#         self.xotira = xotira
#     def hisobla(self):
#         if self.xotira == 1:
#             return f' {self.xotira}TB'
#         elif self.xotira == 2:
#             return f' {self.xotira}TB'
#         else:
#             return f' {self.xotira}GB'
#     def get_info(self):
#         return f'{self.malumot()}{self.brend} {self.model} , xotirasi {self.hisobla()} , narxi {self.narxi}$'
    

# mahsulot1 = Telefon('Smartfon' , 860 , 'Samgung' , 'S25' , 256)
# print(mahsulot1.get_info())



                                                                                            # 9
# class Shaxs:
#     def __init__(self, ism , familiya , yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#         def info(self):
#             return f'{self.familiya} {self.ism} , {self.yil}yil tug\'ilgan'

# class Oqituvchi(Shaxs):
#     def __init__(self, ism, familiya, yil , kasb , tajriba):
#         super().__init__(ism, familiya, yil)
#         self.kasb = kasb
#         self.tajriba = tajriba
#     def get_info(self):
#         return f'{self.familiya} {self.ism} , {self.yil}yil tug\'ilgan , kasbi {self.kasb} va {self.tajriba}yildan buyon shu kasb egasi'
    
# shaxs1 = Oqituvchi('Ali' , 'Aliyev' , 1995 , 'Oqituvchi' , 8)
# print(shaxs1.get_info())



                                                    # 10
# class Mashina:
#     def __init__(self ,turi , rangi):
#         self.turi = turi
#         self.rangi = rangi
#     def malumot(self):
#         return f'{self.turi} {self.rangi} rangi'
    
# class Yuk_mashina(Mashina):
#     def __init__(self, turi, rangi, yuk):
#         super().__init__(turi, rangi)  
#         self.yuk =  yuk 
#     def info(self):
#         return f'{self.malumot()} , oziga {self.yuk} tonna yuk sigdira oladi '
    
# mashina1 =Yuk_mashina('Yuk mashina' , 'Oq' , 13)
# print(mashina1.info())


                                                            # 11
# class Uchuvchi:
#     def __init__(self, ism , familiya , yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#     def malumot(self):
#         return f'{self.familiya} {self.ism} {self.yil}yil tug\'ilgan'

# class Harbiy_uchuvchi(Uchuvchi):
#     def __init__(self, ism, familiya, yil , kasb , tajriba):
#         super().__init__(ism, familiya, yil)
#         self.kasb = kasb
#         self.tajriba = tajriba
#     def info(self):
#         return f'{self.malumot()} , kasbi {self.kasb} va {self.tajriba}yildan buyon {self.kasb}lik kasb egasi'
    
# shaxs1 = Harbiy_uchuvchi('Ali' , 'Aliyev' , 1993 , 'Harbiy uchuvchi' , 4)
# print(shaxs1.info())


                                                            # 12


                                                                    # 13
# class Hayvon:
#     def __init__(self, ovoz):
#         self.ovoz = ovoz
#     def malumot(self):
#         return f'Hayvon ovozi: {self.ovoz}'

# class Mushuk(Hayvon):
#     def __init__(self, ovoz, turi ):
#         super().__init__(ovoz)
#         self.turi = turi 
#     def info(self):
#         return f'Hayvon turi: {self.turi} , va u {self.ovoz} degan ovoz chiqaradi'
    
# class It(Hayvon):
#     def __init__(self, ovoz,turi ):
#         super().__init__(ovoz)
#         self.turi = turi
#     def info(self):
#         return f'Hayvon turi: {self.turi} , va u {self.ovoz} degan ovoz chiqaradi'
    

# hayvon1 = Mushuk('Myau' , 'Mushuk')
# hayvon2 = It('Vouv' , 'It')
# print(hayvon1.info())
# print(hayvon2.info())


                                                                        # 14
# class Texnika:
#     def __init__(self , turi , brend , narx ):
#         self.turi = turi
#         self.brend = brend
#         self.narx = narx
#     def malumot(self):
#         return f'Texnika turi: {self.turi}\n{self.brend} '
    
# class Telefon(Texnika):
#     def __init__(self, turi, brend, narx , model):
#         super().__init__(turi, brend, narx)
#         self.model = model
#     def get_info(self):
#         return f'{self.malumot()} {self.model} , narxi {self.narx}$'

# class Kompyuter(Texnika):
#     def __init__(self, turi, brend, narx , model):
#         super().__init__(turi, brend, narx)
#         self.model = model
#     def get_info(self):
#         return f'{self.malumot()} {self.model} , narxi {self.narx}$'
    
# texnika1 = Telefon('Telefon' , 'POCO'  , 210 , 'X3pro')
# texnika2 = Kompyuter('Kompyuter' , 'Apple' ,1200 , 'MacBook Air')
# print(texnika2.get_info())
# print(texnika1.get_info())



                                            # 15
# class Kompaniya:
#     def __init__(self , nomi , kasbi):
#         self.nomi = nomi
#         self.kasbi = kasbi
#     def malumot(self):
#         return f'{self.nomi}'

# class Ishchi(Kompaniya):
#     def __init__(self, nomi, kasbi , ism , familiya):
#         super().__init__(nomi, kasbi)
#         self.ism = ism
#         self.familiya = familiya
#     def info(self):
#         return f'{self.malumot()} kompaniyasida {self.kasbi} bolib ishlovchi hodim {self.familiya} {self.ism}'

# ishchi1 = Ishchi('Crafers' , 'Meneger' , 'Ali' , 'Aliyev')
# print(ishchi1.info())



# class Avto_dokon:
#         def __init__(self ,  brend , model , narx):   
#                 self.brend = brend
#                 self.model = model
#                 self.narx=  narx
#         def malumot(self):
#                 return f'{self.brend} {self.model}'
        
# class Mashina(Avto_dokon):
#         def __init__(self, brend, model, narx , rang  , probeg):
#                 super().__init__(brend, model, narx)
#                 self.rang =rang
#                 self.probeg = probeg
#         def info(self):
#                 return f'{self.brend} {self.model} narxi {self.narx}$ , {self.rang} rangli , {self.probeg}km yurgan'
# avto1 = Mashina('Mersedes' , 'E63' , '13600' , 'oq' , '142000')
# avto2 = Mashina('KIA' , 'K5' , '35000' , 'oq' , '2000')
# print(avto1.info())
# print(avto2.info())

# yolvchi
                                                                                                # 17
class Transport:
        def __init__(self, nomi , turi , sonli):
                self.nomi = nomi
                self.turi = turi
                self.sonli = sonli
        def malumot(self):
                return f'{self.turi} , {self.nomi} kompamiyasiga tegishli , {self.sonli} sonli poyezd'
class Poyezd(Transport):
        def __init__(self, nomi, turi , uchun , sonli  , vagon):
                super().__init__(nomi, turi , sonli)
                self.uchun = uchun
                self.vagon = vagon
        def 