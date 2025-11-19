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



#                                             15
# class Kompaniya:
#     def __init__(self , nomi , kasbi):
#         self.nomi = nomi
#         self.kasbi = kasbi
# #     def malumot(self):
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
# class Transport:
#         def __init__(self, nomi , turi , sonli):
#                 self.nomi = nomi
#                 self.turi = turi
#                 self.sonli = sonli
#         def malumot(self):
#                 return f'{self.turi}\n{self.nomi} kompamiyasiga tegishli , {self.sonli} sonli {self.turi}.'
# class Poyezd(Transport):
#         def __init__(self, nomi, turi , sonli , uchun , vagon):
#                 super().__init__(nomi, turi , sonli)
#                 self.uchun = uchun
#                 self.vagon = vagon
#         def yonalish(self , qayerdan , qayerga ):
#                 self.qayerdan = qayerdan
#                 self.qayerga = qayerga
#         def bilet(self , narxi):
#                 self.narxi = narxi
#         def get_poezd(self):
#                 return f'{self.malumot()}. Bu poyezd {self.uchun} uchun , {self.vagon}ta vagondan iborat va bu poyezdning yonalishi {self.qayerdan}-{self.qayerga}. Chipta narxi {self.bilet}so\'m.'
        
# class Avtobus(Transport):
#         def __init__(self, nomi, turi, sonli , sigim ,yili):
#                 super().__init__(nomi, turi, sonli)
#                 self.sigim = sigim
#                 self.yili = yili
#         def chipta(self , narx):
#                 self.narx = narx
#         def yonalish(self , qayerdan , qayerga ):
#                 self.qayerdan = qayerdan
#                 self.qayerga = qayerga
#         def get_avtobus(self):
#                 return f'{self.malumot()}. Bu avtobus {self.yili}yil ushlab chiqaarlingan bolib oziga {self.sigim} nafar odam sigdira oladi va bu avtobusning yonalishi {self.qayerdan}-{self.qayerga}. Chipta narxi {self.chipta}so\'m.' 

# transport1 = Poyezd('O\'zTY' , 'Poyezd' , 'W418' , 'yolivchi tashish' , 37)
# transport1.yonalish('Toshkent' , 'Xorazm')
# transport1.bilet(362000)
# print(transport1.get_poezd())



                                                                        # 18
# class Shaxs:
#         def __init__(self , ism , familiya , yil):
#                 self.ism = ism
#                 self.familiya = familiya
#                 self.yil = yil
#         def malumot(self):
#                 return f'{self.familiya} {self.ism} , {self.yil}yil tugilgan.'
        
# class Talaba(Shaxs):
#         def __init__(self, ism, familiya, yil , univer , kurs):
#                 super().__init__(ism, familiya, yil)
#                 self.univer = univer
#                 self.kurs = kurs
#         def fakultet(self , nomi):
#                 self.nomi = nomi
#         def yangilash(self):
#                 self.kursi +=1
#         def end_univer(self):
#                 if self.kursi == 4:
#                         return 'Bitiruvchi talaba'
#         def get_student(self):
#                 return f'{self.malumot()} {self.univer} universitetida {self.nomi} fakultetidan talim oladi , {self.kurs}-kurs'

# class Oqituvchi(Shaxs):
#         def __init__(self, ism, familiya, yil , maktab ):
#                 super().__init__(ism, familiya, yil)
#                 self.maktab = maktab
#         def fan(self, fan_nomi):
#                 self.fan_nomi = fan_nomi
#         def tajriba(self , opit):
#                 self.opit = opit
#         def yangilash(self):
#                 self.opit +=1
#         def get_teacher(self):
#                 return f'{self.malumot()} {self.maktab} maktabida {self.fan_nomi} fanidan talim beradi , {self.opit}yil tajribaga ega'

# shaxs1 = Oqituvchi('ALi' , 'Aliyev' , '1996' , '2-Sizov')
# shaxs1.fan('Makematika')
# shaxs1.tajriba(7)
# shaxs1.yangilash()
# print(shaxs1.get_teacher())


                                                                                        # 19
# class Maxsulot:
#         def __init__(self , nomi , narxi):
#                         self.nomi = nomi
#                         self.narxi = narxi
#                 def malumot(self):
#                         return f'{self.nomi} , narxi {self.narxi}so\'m'
                
#         class Meva(Maxsulot):
#                 def __init__(self, nomi, narxi , turi):
#                         super().__init__(nomi, narxi)
#                         self.turi = turi
#                 def muddat(self , muddat):
#                         self.muddat = muddat
#                 def davlat(self , qayer):
#                         self.qayer = qayer
#                 def get_meva(self):
#                         return f'Maxsulot: {self.nomi}\n{self.turi} , narxi{self.narxi}so\'m. Dokonga {self.muddat}yil {self.qayer} shahridan kelgan.'

#         maxsulot1 = Meva('Meva' , 30000 , 'Marakuya')
#         maxsulot1.muddat('10.27.2025') 
#         maxsulot1.davlat('Avstraliya')
#         print(maxsulot1.get_meva())


# class Bino:
#         def __init__(self  , manzil , narx):
#                 self.manzil = manzil
#                 self.narx = narx
#         def malumot(self):
#                 return f'{self.manzil} , narxi {self.narx}$'
        
# class Uy(Bino):
#         def __init__(self, manzil, kv , narx ,   honalar):
#                 super().__init__(manzil, narx)
#                 self.honalar = honalar
#                 self.kv=  kv
#         def remont(self , remont):
#                 self.remont = remont
#         def xaq(self , turi, uzunlik , balandlik ,  kenglik , kv_narx):
#                 self.turi = turi
#                 self.uzunlik = uzunlik
#                 self.balandlik = balandlik
#                 self.kenglik =  kenglik
#                 self.kv_narx = kv_narx
#         def get_xaq(self):
#                 return f'Xizmat turi: {self.turi}\nXona uzunliki {self.uzunlik}m\nXona kengliki {self.kenglik}m\nXona balantliki: {self.balandlik}m\n1kv narx : {self.kv_narx}$\nJami usta xaqqi: {(self.uzunlik * self.kenglik * self.balandlik) * self.kv_narx}$'
#         def xonalar_maydoni(self , xonalar_maydoni):
#                 self.xonalar_maydoni = xonalar_maydoni
#         def get_info(self):
#                 return f'Manzil: {self.manzil} {self.kv}kv\nNarxi: {self.narx}$\nHonalar soni: {self.honalar}ta\nRemont: {self.remont}.\nXonalar maydoni {self.xonalar_maydoni}m²'
        
# uy1 = Uy('3/8A' , '24' , 30000 , 4)
# uy1.remont('Evro')
# uy1.xaq('Pol taxta' , 8 , 1 , 5 , 2)
# uy1.xonalar_maydoni(20)
# print(uy1.get_xaq())
        

                                                                                # 21
# class Avto:
#         def __init__(self, model, yil, tezlik):
#                 self.model = model
#                 self.yil = yil
#                 self.tezlik = tezlik

#         def info(self):
#                 return f"Model: {self.model}\nYil: {self.yil}yil\nTezlik: {self.tezlik}km/h"


# class SportAvto(Avto):
#         def __init__(self, model, yil, tezlik, turi):
#                 super().__init__(model, yil, tezlik)
#                 self.turi = turi

#         def get_info(self):
#                 return f'{self.info()}\nMashina turi: {self.turi}'
        

# sport = SportAvto("BMW M5", 2023, 330, 'Turbo')
# print(sport.get_info())

                                                                                # 22
# class Kitob:
#         def __init__(self, nomi, muallif, sahifa):
#                 self.nomi = nomi
#                 self.muallif = muallif
#                 self.sahifa = sahifa

#         def malumot(self):
#                 return f"Nomi: {self.nomi}\nMuallif: {self.muallif}\nSahifa: {self.sahifa}bet"


# class ElektronKitob(Kitob):
#         def __init__(self, nomi, muallif, sahifa_soni, fayl_hajmi, formati):
#                 super().__init__(nomi, muallif, sahifa_soni) 
#                 self.fayl_hajmi = fayl_hajmi
#                 self.formati = formati

#         def info(self):
#                return f'{self.malumot()}\nFayl hajmi: {self.fayl_hajmi}MB\nKitob formati: {self.formati}'
        

# kitob = ElektronKitob('Layli va Majnun' , 'Alisher Navoi', 450, 8, "Elektron")
# print(kitob.info())


                                                                                        # 23
# class Avto:
#     def __init__(self , brend ,  model , yil ):
#         self.brend  = brend
#         self.model = model
#         self.yil = yil

#     def malumot(self):
#         return f"{self.brend} {self.model}, {self.yil}yil ishlab chiqarlingan"

# class Elektro_Avto(Avto):
#     def __init__(self, brend, model, yil , batareya):
#         super().__init__(brend, model, yil)
#         self.batareya = batareya

#     def zaryad_qoshish(self, foiz):
#         self.foiz = foiz
#         return f"Mashinang zaryadlangandan keyingi zaryadi:{self.batareya + self.foiz}%"

#     def zaryad_foiz(self):
#         return f"Hozirgi batareya darajasi: {self.batareya}%"

#     def get_info(self):
#         return f'{self.brend} {self.model}, {self.yil}yil ishlab chiqarlingan , mashinaning zaryadi: {self.batareya}%'


# avto1 = Elektro_Avto('BYD' , 'Chempion' , 2024  , 45)
# print(avto1.get_info())
# print(avto1.zaryad_qoshish(30))


                        # 24
# class Son:
#     def __init__(self , a , b):
#         self.a = a
#         self.b = b

# class Hisobla(Son):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def qosh(self):
#         return f'{self.a} ga {self.b} ni qoshsa {self.a + self.b} boladi'
    
#     def ayir(self):
#         return f'{self.a} dan {self.b} ni ayirsa {self.a - self.b} boladi'
    
#     def kopaytir(self):
#         return f'{self.a} ga {self.b} ga kopaytirsa {self.a * self.b} boladi'
    
#     def bol(self):
#         return f'{self.a} ni {self.b} ga bolsa {self.a / self.b} boladi'
    
# son1 = Hisobla(5,4)
# print(son1.kopaytir())


                                                                                    # 25
# class Hayvon:
#     def __init__(self, turi):
#         self.turi = turi

#     def malumot(self):
#         return f'Hayvon turi: {self.turi}'

# class Qush(Hayvon):
#     def __init__(self , turi  ,nomi):
#         super().__init__(turi)
#         self.nomi = nomi

#     def uchish(self , qanot_uzunligi):
#         self.qanot_uzunligi = qanot_uzunligi  
#         return f"{self.nomi} {self.qanot_uzunligi}sm qanot bilan uchmoqda."

#     def tovush(self , tuvush):
#         self.tuvush = tuvush
#         return f"{self.nomi} {self.tuvush} tovush chiqarmoqda."
#     def info(self):
#         return f'{self.malumot()} {self.nomi}'


# hayvon1 = Qush('Qush' , 'Lochin')
# print(hayvon1.info())
# print(hayvon1.uchish(45))
# print(hayvon1.tovush('Lochin ovozi'))

                                                                        # 26

# class Maktab:
#     def __init__(self, maktab_nomi, manzil , talim):
#         self.maktab_nomi = maktab_nomi
#         self.manzil = manzil
#         self.talim = talim
#         self.sinflar = []    

#     def sinf_qoshish(self , sinf_nomi):
#         self.sinf_nomi = sinf_nomi
#         self.sinflar.append(sinf_nomi)
#         return f"'{self.sinf_nomi}' {self.maktab_nomi} maktabiga qoshildi."

#     def mk_info(self):
#         return f"Maktab: '{self.maktab_nomi}'\nTalim: {self.talim}\nManzil: {self.manzil}\nSinflar soni: {len(self.sinflar)}"


# class Sinf(Maktab):
#     def __init__(self, maktab_nomi, manzil , talim):
#         super().__init__(maktab_nomi, manzil , talim)
#         self.oquvchilar = []
#         self.oquvchilar_soni = 0
#         self.darslar = []

#     def oquvchi_qoshish(self, oquvchi_ismi):
#         self.oquvchi_ismi = oquvchi_ismi
#         self.oquvchilar.append(oquvchi_ismi)
#         self.oquvchilar_soni +=1
#         return f"{self.sinf_nomi} sinfiga {self.oquvchi_ismi} qoshildi.\n{self.sinf_nomi} sinfidagi oquvchilar soni {self.oquvchilar_soni} va ular {self.oquvchilar}"

#     def dars_qoshish(self, dars_nomi):
#         self.dars_nomi = dars_nomi
#         self.darslar.append(dars_nomi)
#         return f"{self.dars_nomi} fani {self.sinf_nomi}ga qoshildi.\n{self.sinf_nomi} sinfida darslar royhadi {self.darslar}"

#     def class_info(self):
#         return f"\tSinf haqida malumot\nSinf nomi: {self.sinf_nomi}\nOquvchilar: {self.oquvchilar}\nDarslar: {self.darslar}"
#     def maktab_info(self):
#         return f'\tMaktab haqida malumot\n{self.mk_info()}'

# sinf1 = Sinf('2-maktab' , 'Tuproqqala' , 'Orta talim')
# sinf1.sinf_qoshish('8B')
# sinf1.oquvchi_qoshish('Ali')
# sinf1.oquvchi_qoshish('Laylo')
# sinf1.dars_qoshish('Matematika')
# sinf1.dars_qoshish('Informatika')
# print(sinf1.maktab_info())
# print(sinf1.class_info())


            # 27
# class Avto:
#     def __init__(self, brend , model, yil , mator , narx):
#         self.brend = brend
#         self.model = model
#         self.yil = yil
#         self.mator = mator
#         self.narx = narx

#     def info(self):
#         return f"{self.brend} {self.model}, mator hajmi {self.mator}L {self.yil}yil ishlab chiqarlingan, narxi {self.narx}$"


# class Mercedes(Avto):
#     def __init__(self, brend , model, yil , mator , narx , rejim):
#         super().__init__(brend , model, yil , mator , narx)
#         self.rejim = rejim 

#     def benzin_sarf(self , km_sarf):
#         self.km_sarf = km_sarf
#         return f'{self.brend} {self.model} mashinasi 100km uchun {self.km_sarf * 100}l benzin kerak'

#     def mers_info(self):
#         return  f'{self.info()}\nRejim: {self.rejim}\n'


# class Chevrolet(Avto):
#     def __init__(self, brend , model, yil , mator , narx , rejim):
#         super().__init__(brend , model, yil, mator , narx)
#         self.rejim = rejim 

#     def benzin_sarf(self , km_sarf):
#         self.km_sarf = km_sarf
#         return f'{self.brend} {self.model} mashinasi 100km uchun {self.km_sarf * 100}l benzin sarf qiladi'

#     def cevrolet_info(self):
#         return  f'{self.info()}\nRejim: {self.rejim}\n'

# avto1 = Mercedes('Mersedes',  'W124' , 1996 , '4,2' , 14000 , 'Classic')
# print(avto1.mers_info())
# print(avto1.benzin_sarf(3))


                            # 28
# class Texnika:
#     def __init__(self, model, narx):
#         self.model = model
#         self.narx = narx

#     def info(self):
#         return f"Model: {self.model}, Narx: {self.narx}$"


# class Printer(Texnika):
#     def __init__(self, model, narx, qanaqa):
#         super().__init__(model, narx)
#         self.qanaqa = qanaqa  

#     def print_qil(self, matn):
#         self.matn = matn
#         if self.qanaqa == 'rangli':
#             return f"Rangli printer '{self.model}' {self.matn}ni chop etmoqda "
#         else:
#             return f"Oq-qora printer '{self.model}' {self.matn}ni chop etmoqda "
#     def pr_info(self):
#         return f'{self.info()}. {self.qanaqa} printer'
    


# class Skanner(Texnika):
#     def __init__(self, model, narx, dpi):
#         super().__init__(model, narx)
#         self.dpi = dpi

#     def scan_qil(self):
#         return f"Skanner '{self.model}' {self.dpi} DPI sifatda hujjatni skan qildi."
#     def sr_info(self):
#         return f'{self.info()}. {self.dpi}DPI skaner'

# texnika1 = Skanner('R28' , 60 , 9000)
# print(texnika1.scan_qil())
# print(texnika1.sr_info())

            # 29
# class Sportchi:
    
#     def __init__(self,familiya , ism, yosh , sport_turi):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.sport_turi = sport_turi
        
#     def malumot(self):
#         return f"Sport Turi: {self.sport_turi}\nIsm familiyasi:{self.familiya} {self.ism}\nYosh: {self.yosh}\n"


# class Futbolchi(Sportchi): 
#     def __init__(self,familiya , ism , yosh , sport_turi , pozitsiya , jamoa):
#         super().__init__(familiya ,ism , yosh, sport_turi)
#         self.pozitsiya = pozitsiya
#         self.jamoa = jamoa
#         self.gollar_soni = 0  
        
#     def gol_urish(self):
#         self.gollar_soni += 1
#         return f'{self.ism} gol urdi Uning gollari soni: {self.gollar_soni}'
        
#     def transfer_bolish(self, yangi_jamoa):
#         eski_jamoa = self.jamoa
#         self.yangi_jamoa = yangi_jamoa
#         return f' {self.familiya} {self.ism} {eski_jamoa} dan {self.yangi_jamoa} ga transfer qilindi.'

#     def info(self):
#         return f'{self.malumot()}Pozitsiya: {self.pozitsiya}\nJamoa: {self.jamoa}\nGollari: {self.gollar_soni}ta'



# futbolchi1 = Futbolchi("Robert" ,  'Lewandovski', 36 , 'Futbolchi' , 'Hujumchi', 'Barselona')

# futbolchi1.gol_urish()
# futbolchi1.gol_urish()
# futbolchi1.gol_urish()
# print(futbolchi1.info())
# print(futbolchi1.transfer_bolish("AS Milan"))



                # 30
# class Student:
#     def __init__(self, ism , familiya , yonalish , kurs):
#         self.ism = ism
#         self.familiya = familiya
#         self.yonalish = yonalish
#         self.kurs = kurs 
#     def malumot(self):
#         return f'{self.familiya} {self.ism} {self.kurs}-kursda {self.yonalish} yonalishida talim oladi.'
    
# class Talaba(Student):
#     def __init__(self, ism, familiya, yonalish, kurs , fan , ball , ):
#         super().__init__(ism, familiya, yonalish, kurs)
#         self.fan = fan
#         self.ball = ball
#         self.kontrakt = 15000000
#     def count_ball(self):
#         if 30<=self.ball>=66:
#             return f'{self.familiya} {self.ism} ning bahosi qoniqarli'
#         elif 67<=self.ball>=85:
#             return f'{self.familiya} {self.ism} ning bahosi yaxshi'
#         elif 86<=self.ball>=100:
#             return f'{self.familiya} {self.ism} ning bahosi a\'lo'
#         elif 0<=self.ball>=29:
#             return f'{self.familiya} {self.ism} ning bahosi qoniqarsiz'
#         else:
#             return f'Xatolik!!!'
        
#     def count_gpa(self):
#         gpa = sum({self.ball}) // len({self.fan})
#         return f'{self.familiya} {self.ism}ning ortacha ball {gpa}'
    
#     def talim_turi(self , talim_turi , stipendiya , qancha_toladi):
#         if talim_turi.lower() == "grand":
#             if self.ball >=60:
#                 return f"{self.familiya} {self.ism} imtihonga kirishiga ruhsat"
#             else:
#                 return f"{self.familiya} {self.ism} grandda o'qiydi lekin ball yetmagani sababli imtihonga qo'yilmaydi"
#         elif talim_turi == "kontrakt":
#             if stipendiya.lower() == 'stipendiyali':
#                 if self.kontrakt *60 /100 <= qancha_toladi:
#                     if self.ball >= 60:
#                         return f"{self.familiya} {self.ism} imtihonga kirishiga ruhsat"
#                     else:
#                         return f"{self.familiya} {self.ism} kontrank pulingiz tolangan lekin balingiz yetmaydi"
#                 else: 
#                     return f'{self.familiya} {self.ism} kontrank pulingizni tolang'
#         else:
#             return f'Talim turini togri kiriting'


# talaba1 = Talaba('Ali' , 'Aliyev' , 'Filologiya' , 2 , 'Matematika' , 55 )
# print(talaba1.count_ball())
# print(talaba1.talim_turi('kontrakt' , 'stipendiyali' , 12000000 ))


class Avto:
    def __init__(self , brend , model , yil , narx):
        self.brend = brend
        self.model = model
        self.yil = yil
        self.narx = narx
    def info(self):
        return f'{self.brend} {self.model} , {self.yil}yil , narxi {self.narx}$'