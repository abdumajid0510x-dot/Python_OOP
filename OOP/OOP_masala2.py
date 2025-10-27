                                                                # 1
# class Student:
#     def __init__(self , ism , yosh , baho):
#         self.ism = ism
#         self.yosh = yosh
#         self.baho = baho
#     def info(self):
#         return f'Student ismi {self.ism} , uning yoshi {self.yosh}da va uning bahosi: {self.baho}'
# student1 = Student('Ali' , 21 , 4)
# print(student1.info())

                                                                # 2
# class Mashina:
#     def __init__(self,madel,yil,rang):
#         self.madel = madel
#         self.yil = yil
#         self.rang =rang
#     def get_info(self):
#         return print(f'{self.madel} - modeli , {self.yil} - yili , {self.rang} - rang')

# class Bozor:
#     def __init__(self,bozor):
#         self.bozor = bozor
#         self.mashinalar_soni = 0
#         self.royhat = []
#     def add_car(self,madel,yili,rang):
#         mashina = Mashina(madel,yili,rang)
#         self.royhat.append(mashina)
#         self.mashinalar_soni+= 1
#     def avto_info(self):
#         car = "\n".join([avto.get_info() for avto in self.royhat])
#         return f'Bozorimizda {self.mashinalar_soni} ta moshina bor \n{car} \n'
    

# mashina1 = Bozor('GM avto')
# mashina1.add_car('Gentra' , 2022, 'Qora')
# mashina1.add_car('Tahoe' , 2025 , 'Qora')
# mashina1.add_car('Chiron' , 2016 , 'Ko\'k')

# print(mashina1.avto_info())
                                        # 3
# class Hisobraqam:
#     def __init__(self , balans):
#         self.balans = balans
#     def pul_qosh(self , pul_miqdori):
#         self.pul_miqdori = pul_miqdori
#         self.balans += self.pul_miqdori
#         return f'Sizning balansizngizga {self.pul_miqdori}$ pul qoshildi va sizning balansingiz {self.balans}$ pul bor'
#     def pul_ol(self, qiymati):
#         self.qiymati = qiymati
#         if self.balans < self.qiymati:
#             return f'{self.qiymati - self.balans}$ pul yetmaydi'
#         else:
#             self.balans -= self.qiymati
#             return f'Sizning hisobingizdan {self.qiymati}$ pul yechib olinda va sizning balansingizda {self.balans}$ pul qoldi'
#     def otccot(self):
#         return f'Hozirda sizning hisobingizda {self.balans}$ pul bor'
# ali = Hisobraqam(300)
# print(ali.pul_ol(70))
# print(ali.pul_qosh(270))

# class Maxsulot:
#     def __init__(self , maxsulot_nomi , kg_narx):
#         self.maxsulot_nomi = maxsulot_nomi
#         self.kg_narx = kg_narx
#     def malumot(self):
#         return f'{self.maxsulot_nomi} , narxi: {self.kg_narx}so\'m'
# class Dokon:
#     def __init__(self, dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.royhat = []
#     def add_maxsulot(self , maxsulot_nomi , kg_narx):
#         maxsulotlar = Maxsulot(maxsulot_nomi , kg_narx)
#         self.royhat.append(maxsulotlar)
#     def info(self):
#         product = " \n".join([produkta.malumot() for produkta in self.royhat])
#         return f"Bizning {self.dokon_nomi} nomli do'konimizda mavjud bolgan maxshulotlar \n{product}\n "
# dokon1 = Dokon('Eco bozor')
# dokon1.add_maxsulot('Shakar' , 16000)
# dokon1.add_maxsulot('Olma' , 6000)
# dokon1.add_maxsulot('Yog\'' , 14000)

# print(dokon1.info())


                                                # 5
# class Ishchi:
#     def __init__(self, ism , familiya , tuglgan_yili):
#         self.ism = ism
#         self.familiyas = familiya
#         self.tuglgan_yili = tuglgan_yili
#     def worker_info(self):
#         return f'{self.familiyas} {self.ism} va tugilgan yili {self.tuglgan_yili} '

# class Kompayina:
#     def __init__(self , kompayina_nomi ): 
#         self.kompayina_nomi = kompayina_nomi
#         self.royhat = []
#     def add_worker(self ,ism , familiya , tuglgan_yili):
#         ishchilar = Ishchi(ism, familiya,  tuglgan_yili)
#         self.royhat.append(ishchilar)
#     def get_info(self):
#         work = "\n".join([ish.worker_info() for ish in self.royhat])
#         return f'Bizning {self.kompayina_nomi} kompaniyamizda ishlaydigan ishchilar \n{work}\n'
    
# kompayina1 = Kompayina('IT park')
# kompayina1.add_worker('Xusainov' , 'Mirzabek' , 2000)
# kompayina1.add_worker('Nodir' , 'ustoz'  , 1998)
# kompayina1.add_worker('Azamat' , 'ustoz' , 1997)
# print(kompayina1.get_info())


# class Mashina:
#     def __init__(self,  model , tezlik):
#         self.model = model
#         self.tezlik = tezlik
#     def tezlik_qosh(self, qancha):
#         self.qancha = qancha
#         self.tezlik += self.qancha
#         return f'Mashinaning tezligiga {self.qancha}km/s tezlik qoshildi va uning tezligi {self.tezlik}km/s ga teng boldi'
#     def tezlik_ol(self , miqdori):
#         self.miqdori = miqdori
#         if self.tezlik < self.miqdoti:
#             return f'Sizning kiritgan tezligingiz xozirgi  mashina tezligidan katta'
#         else:
#             self.tezlik -= self.miqdori
#             return f'Mashina tezligidan {self.miqdori}km/s tezlik olindi va mashina tezligi {self.miqdori}km/s ga tushti'

#     def info(self):
#         return f'Va mashinaning hozirgi tezligi {self.tezlik}km/s'

# mashina1 = Mashina('E63' , 60)
# print(mashina1.tezlik_qosh(30))
# print(mashina1.info())



                                                                # 7
# import time
# class Telefon:
#     def __init__(self , brend , nom , batareya):
#         self.brend = brend
#         self.nom = nom
#         self.batareya = batareya
#     def tel_zaryadlash(self):
#         while True:
#             self.batareya +=1
#             time.sleep(5)
#             print (f'Talingiz zaryadi {self.batareya}% va u {((100-self.batareya)*5)/60} munutda toladi')
#             if self.batareya == 100:
#                 break
#     def malumot(self):
#         return f'{self.brend} {self.nom} nomli telning zaryadi {self.batareya}'

# tel1 = Telefon('Samsung' , 'S25' , 15)
# print(tel1.malumot())
# print(tel1.tel_zaryadlash())  

                                                                # 8
# class Oqtuvchi:
#     def __init__(self , ism , fan, tajriba):
#         self.ism = ism
#         self.fan = fan
#         self.tajriba = tajriba
#     def info(self):
#         return f'Ismi: {self.ism}\nFani: {self.fan}\nTajribasi: {self.tajriba}yil\n'

# oqtuvchi1 = Oqtuvchi('Mirzabek' , 'IT va Informatika' , 7)
# print(oqtuvchi1.info())


                                                    # 9
# class Kompyuter:
#     def __init__(self , brend , ram , hdd , cpu):
#         self.brend = brend
#         self.ram = ram
#         self.hdd = hdd
#         self.cpu = cpu
#     def info(self):
#         return f'Brend: {self.brend}\nRAM: {self.ram}GB\nHDD: {self.hdd}GB\nCPU: {self.cpu}CPU'
# komp1 = Kompyuter('Lenovo' , 16 , 512 , 8)
# print(komp1.info())



                                                                                    # 10
# class Oquvchi:
#     def __init__(self , ismi ,familiyasi, sinfi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.sinfi = sinfi
#     def malumot(self):
#         return f'{self.familiyasi} {self.ismi} , {self.sinfi}-sinfda talim oladi'

# class Sinf:
#     def __init__(self , sinf):
#         self.sinf = sinf
#         self.royhat = []
#     def add_students(self , ismi ,familiyasi, sinfi):
#         oquvchilar = Oquvchi(ismi ,familiyasi, sinfi)
#         self.royhat.append(oquvchilar)
#     def info(self):
#         student = "\n".join([oquvchi.malumot() for oquvchi in self.royhat])
#         return f'{self.sinf} sinfida talim oladigan oquvchilar: \n{student}\n'

# sinf1 = Sinf('8-B')   
# sinf1.add_students('Ali' , 'Aliyev' , 8)
# sinf1.add_students('Vali' , 'Valiyev' , 8)
# print(sinf1.info())



                                                        # 11
# class Shaxs:
#     def __init__(self , ism , yosh , qiziqish):
#         self.ism = ism
#         self.yosh = yosh
#         self.qiziqish = qiziqish
#     def malumot(self):
#         return f'{self.ism} yoshi {self.yosh}da , {self.qiziqish}ga qiziqadi.'

# class Tanishtir:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_person(self , ism , yosh , qiziqish):
#         shaxs = Shaxs(ism , yosh , qiziqish)
#         self.royhat.append(shaxs)
#     def  info(self):
#         people = "\n".join([odam.malumot() for odam in self.royhat])
#         return f'Bizning {self.nomi} nomli platformamizda siz bu shaxslar bilan tanishishingiz mumkun: \n{people}\n'

# shaxs1 = Tanishtir('Tanishtir') 
# shaxs1.add_person('Ali' , '23' , 'IT')
# shaxs1.add_person('Vali' , '19' , 'Ingliz tili')
# print(shaxs1.info())



                                                                        # 13
# class Kitob:
#     def __init__(self , nom, muallif , sahifa ):
#         self.nom = nom
#         self.muallif = muallif
#         self.sahifa = sahifa
#     def malumot(self):
#         return f'Kitob nomi: {self.nom}\nKitob muallifi: {self.muallif}\nKitob sahifasi: {self.sahifa}bet\n\n'

# class Kitobqosh:
#     def __init__(self):
#         self.royhat = []
#     def add_book(self , nom, muallif , sahifa):
#         kitob = Kitob(nom, muallif , sahifa)
#         self.royhat.append(kitob)
#     def info(self):
#         kniga = "".join([i.malumot() for i in self.royhat])
#         return f'Bizda mavjud bolgan kitoblar: \n{kniga}\n'
    
# kitob1 = Kitobqosh()
# kitob1.add_book('Stiv Jobs' ,  'Stiv Jobs' , 140)
# kitob1.add_book('Dastoevskiy' , 'Dastoevskiy' , 88)
# print(kitob1.info())


                                            # 14
# class Kitob:
#     def __init__(self , nom, muallif , yili ):
#         self.nom = nom
#         self.muallif = muallif
#         self.yili = yili
#     def malumot(self):
#         return f'Kitob nomi: {self.nom}\nKitob muallifi: {self.muallif}\nKitob {self.yili}-yilda ishlab chiqarlingan\n'

# class Kutubxona:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_book(self , nom, muallif , yili):
#         kitob = Kitob(nom, muallif , yili)
#         self.royhat.append(kitob)
#     def info(self):
#         kniga = "\n".join([i.malumot() for i in self.royhat])
#         return f'Bizning {self.nomi} nomli kutubxonamizda mavjud bolgan kitoblar: \n{kniga}\n'
    
# kutubxona1 = Kutubxona('Knijniy')
# kutubxona1.add_book('Aleksandr Pushkin' ,  'Aleksandr Pushkin' , 1834)
# kutubxona1.add_book('Lev Tolstoy' , 'Lev Tolstoy' , 1769)
# print(kutubxona1.info())



                                    # 15
# class Maxsulot:
#     def __init__(self , maxsulot_nomi , kg_narx):
#         self.maxsulot_nomi = maxsulot_nomi
#         self.kg_narx = kg_narx
#     def malumot(self):
#         return f'{self.maxsulot_nomi} , narxi: {self.kg_narx}so\'m'
# class Dokon:
#     def __init__(self, dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.royhat = []
#     def add_maxsulot(self , maxsulot_nomi , kg_narx):
#         maxsulotlar = Maxsulot(maxsulot_nomi , kg_narx)
#         self.royhat.append(maxsulotlar)
#     def info(self):
#         product = " \n".join([i.malumot() for i in self.royhat])
#         return f"Bizning {self.dokon_nomi} nomli do'konimizda mavjud bolgan maxshulotlar \n{product}\n "
# dokon1 = Dokon('Magnit')
# dokon1.add_maxsulot('Tuxum 15ta' , 22000)
# dokon1.add_maxsulot('Un' , 6000)


# print(dokon1.info())


                                                            # 17
# class Uy:
#     def __init__(self,  manzil , xona):
#         self.manzil = manzil
#         self.xona = xona
#     def malumot(self):
#         return f'Manzil: {self.manzil} , {self.xona}xonali'
    
# class Uyqosh:
#     def __init__(self ):
#         self.royhat = []
#     def add_home(self , manzil , xona):
#         uy = Uy(manzil , xona)
#         self.royhat.append(uy)
#     def info(self):
#         uylar = "\n".join([i.malumot() for i in self.royhat])
#         return f'Hozir sotuvda mavjud bolgan uylar: \n{uylar}\n'
# uy1= Uyqosh()
# uy1.add_home('3/8dom 14uy', 3) 
# print(uy1.info())



                                # 18
# class Shaxs:
#     def __init__(self , ism ):
#         self.ism = ism
#     def malumot(self):
#         return f'Oilangizga {self.ism} qoshildi'

# class Oila:
#     def __init__(self , nomi): 
#         self.nomi = nomi
#         self.royhat = []
#         self.odam_soni = 0
#     def add_person(self , ism):
#         shaxs = Shaxs(ism)
#         self.royhat.append(shaxs)
#         self.odam_soni += 1
#     def info(self):
#         oila_azolar = '\n'.join([i.malumot() for i in self.royhat]) 
#         return f'{self.nomi}lar oilasida {self.odam_soni} nafar odam bor va ular: \n{oila_azolar}\n'

# oila1= Oila('Samandarov')
# oila1.add_person('Muhammad')
# oila1.add_person('Aziz')
# print(oila1.info())




                                                        # 19
# class Sportchi:
#     def __init__(self, ism , turi):
#         self.ism = ism
#         self.turi = turi
#     def malumot(self):
#         return  f'{self.ism}, {self.turi}'
    
# class Info:
#     def __init__(self , qayerda , orin):
#         self.qayerda = qayerda
#         self.orin = orin
#         self.royhat = []
#     def add_info(self , ism , turi):
#         sportchi = Sportchi(ism , turi)
#         self.royhat.append(sportchi)
#     def get_info(self):
#         sport = "".join([i.malumot() for i in self.royhat])
#         return f'\n{sport}\n{self.qayerda}da {self.orin}-orinni oldi'

# sportchi1 = Info('Xorazm' , 1)
# sportchi1.add_info('Abduvaid' , 'Baksyor')
# print(sportchi1.get_info())



                                    # 20
# class Sportchi:
#     def __init__(self , ismi , familiyasi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#     def malumot(self):
#         return f'{self.familiyasi} {self.ismi}'
    
# class Stadion:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_sportsmen(self , ismi , familiyasi):
#         sportchi = Sportchi(ismi , familiyasi)
#         self.royhat.append(sportchi)
#     def get_info(self):
#         sportsmen = "\n".join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} dagi sportsmenlar: \n{sportsmen}\n'

# stadion1 = Stadion('Alianz Arena')
# stadion1.add_sportsmen('Manuel','Nouer')
# stadion1.add_sportsmen('Tomas' , 'Muller')
# print(stadion1.get_info())


                                                                        # 21
# class Ishchi:
#     def __init__(self, ismi, familiyasi , yoshi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi    
#         self.yoshi = yoshi
#     def malumot(self):
#         return f'{self.familiyasi} {self.ismi} , {self.yoshi} yoshda'

# class Kompaniya:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_worker(self, ismi, familiyasi , yoshi):
#         ishchi = Ishchi(ismi, familiyasi , yoshi)
#         self.royhat.append(ishchi)
#     def info(self):
#         work = "\n".join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} da ishlaydigan ishchilar: \n{work}\n'

# kompaniya1 = Kompaniya('GM avto')
# kompaniya1.add_worker('Ali' , 'Aliyev' , 25)
# kompaniya1.add_worker('Vali' , 'Valiyev' , 30)
# print(kompaniya1.info())


                                                                    # 22
# class Kino:
#     def __init__(self, nomi , janr , davomiylik):
#         self.nomi = nomi
#         self.janr = janr
#         self.davomiylik = davomiylik
#     def malumot(self):
#         return f'Kino nomi: {self.nomi} \nKino janri: {self.janr} \nKino davomiyligi: {self.davomiylik}soat'

# class Kinoqosh:
#     def __init__(self):
#         self.royhat = []
#         self.kinolar_soni = 0
#     def add_film(self , nomi , janr , davomiylik):
#         kino = Kino(nomi , janr , davomiylik)
#         self.royhat.append(kino)
#         self.kinolar_soni +=1
#     def info(self):
#         film = "\n".join([i.malumot() for i in self.royhat])
#         return f'Kinoteatrimizda mavjud bolgan kinolar: \n{film}\n\n'

# kino1 = Kinoqosh()
# kino1.add_film('Pushti pantera' , 'Komediya' , '2:40')
# print(kino1.info())



                                                        # 23
# class Kino:
#     def __init__(self, nomi , janr , davomiylik):
#         self.nomi = nomi
#         self.janr = janr
#         self.davomiylik = davomiylik
#     def malumot(self):
#         return f'Kino nomi: {self.nomi} \nKino janri: {self.janr} \nKino davomiyligi: {self.davomiylik}soat'

# class Kinoteatr:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#         self.kinolar_soni = 0
#     def add_film(self , nomi , janr , davomiylik):
#         kino = Kino(nomi , janr , davomiylik)
#         self.royhat.append(kino)
#         self.kinolar_soni +=1
#     def info(self):
#         film = "\n".join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} nomli kinoteartrrida mavjud bolgan kinolar: \n{film}\n\n'

# kino1 = Kinoteatr('Kino')
# kino1.add_film('Pushti pantera' , 'Komediya' , '2:40')
# print(kino1.info())



                                                                # 24
# class Oqituvchi:
#     def __init__(self , familiya , ismi , fan):
#         self.familiya = familiya
#         self.ismi = ismi
#         self.fan = fan
#     def malumot(self):
#         return f'{self.familiya} {self.ismi} , {self.fan} fani oqituvchisi'
    
# class Maktab:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_worker(self , familiya , ismi , fan):
#         oqituvchi = Oqituvchi(familiya , ismi , fan)
#         self.royhat.append(oqituvchi)
#     def info(self):
#         worker = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} nomli maktabdagi oqituvchilar: \n{worker}\n'
    
# maktab1 = Maktab('Sizov')
# maktab1.add_worker('Aliyev' , 'Ali' , 'matematika')
# maktab1.add_worker('Valiyev' , 'Vali' , 'informatika')
# print(maktab1.info())


                                                                            # 25
# class Fakultet:
#     def __init__(self , nomi):
#         self.nomi = nomi
#     def malumot(self):
#         return f'{self.nomi} fakulteti'
    
# class Univer:
#     def __init__(self , uni_nomi):
#         self.uni_nomi = uni_nomi
#         self.royhat = []
#     def add_fakultet(self , nomi):
#         fakultet = Fakultet(nomi)
#         self.royhat.append(fakultet)
#     def info(self):
#         yonalish = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.uni_nomi} nomli universitetimizda mavjud bolgan fakultetlar: \n{yonalish}\n'
    
# univer1 = Univer('UrDU')
# univer1.add_fakultet('Filologiya')
# univer1.add_fakultet('Iqsodiyot')
# print(univer1.info())



                                            # 26
# class Avto:
#     def __init__(self , brend , model , probeg , yil):
#         self.brend = brend
#         self.model = model
#         self.probeg = probeg
#         self.yil =yil
#     def malumot(self):
#         return f'{self.brend} {self.model} {self.probeg}km yurgan , {self.yil}yili ishlab chiqarlingan'
    
# class Avtosalon:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#         self.mashina_soni = 0
#     def add_car(self, brend , model , probeg , yil):
#         avto = Avto(brend , model , probeg , yil)
#         self.royhat.append(avto)
#         self.mashina_soni +=1
#     def info(self):
#         mashina = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} nomli avtosalonda xozirda {self.mashina_soni}ta mashina bor: \n{mashina}\n'
    
# avtosalon1 = Avtosalon('Drujba avto')
# avtosalon1.add_car('Cevrolet' , 'Tohoe' , 12000 , 2024)
# avtosalon1.add_car('Mersedes' , 'E63' , 50000 , 2012)
# print(avtosalon1.info())


                                                                            # 27
# class Shifokor:
#     def __init__(self , ism ,familiya , ishi , tajriba):
#         self.ism = ism
#         self.familiya = familiya
#         self.ishi = ishi
#         self.tajriba = tajriba
#     def malumot(self):
#         return f'{self.familiya} {self.ism} {self.ishi} bolib ishlaydi , {self.tajriba}yil tajribaga ega'
    
# class Kasalxona:
#     def __init__(self , nomi):
#         self.nomi = nomi
#         self.royhat = []
#     def add_worker(self , ism ,familiya , ishi , tajriba):
#         shifokor = Shifokor(ism ,familiya , ishi , tajriba)
#         self.royhat.append(shifokor)
#     def info(self):
#         ishchi = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.nomi}dagi shifokorlar: \n{ishchi}\n'

# kasalxona1= Kasalxona('Tuman kasalxonasi')
# kasalxona1.add_worker('Ali' ,'Aliyev' , 'xirurg' , 9)
# kasalxona1.add_worker('Vali' , 'Valiev' , 'Stamatolog' , 6)
# print(kasalxona1.info())



                                                            # 28
# class Oyinchi:
#     def __init__(self , nik , level , ball):
#         self.nik = nik
#         self.level = level
#         self.ball= ball
#     def info(self):
#         return f'Oyinchi: {self.nik}\nLevel: {self.level}\nBall: {self.ball}\n\n'
    
# oyinchi1 = Oyinchi('Pirate' , 82 , 94)
# print(oyinchi1.info())



                                                                        # 29
# class Oyinchi:
#     def __init__(self , nik , level , ball):
#         self.nik = nik
#         self.level = level
#         self.ball= ball
#     def malumot(self):
#         return f'Oyinchi: {self.nik}\nLevel: {self.level}\nBall: {self.ball}\n\n'
    
# class Oyin:
#     def __init__(self,  nomi):
#         self.nomi= nomi
#         self.royhat= []
#     def add_gamer(self, nik , level , ball):
#         oyinchi = Oyinchi(nik , level , ball)
#         self.royhat.append(oyinchi)
#     def info(self):
#         gamer = '\n'.join([i.malumot() for i in self.royhat])
#         return  f'{self.nomi} oyinini oynaydigan oyinchilar: \n{gamer}\n'
    
# oyin1 = Oyin('CS2')
# oyin1.add_gamer('Pirate' , 82 , 93)
# print(oyin1.info())

                                                                                # 30
# class Taom:
#     def __init__(self ,nomi , narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#     def malumot(self):
#         return f'{self.nomi} , {self.narxi}so\'m'

# class Restoran:
#     def __init__(self , res_nomi):
#         self.res_nomi = res_nomi
#         self.royhat = []
#     def add_food(self, nomi , narxi):
#         taom = Taom(nomi , narxi)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.res_nomi} restorani menyusi: \n{food}\n'

# restoran1 = Restoran('Gavhar')
# restoran1.add_food('Tuxum barak' ,'40000')
# restoran1.add_food('Go\'mma',  '35000')
# print(restoran1.info())



                                                                        #     31
# class Taom:
#     def __init__(self, nom , narx  , kaloriya):
#         self.nom=  nom
#         self.narx = narx
#         self.kaloriya = kaloriya
#     def malumot(self):
#         return f'{self.nom} , narxi {self.narx}so\'m'
    
# class Taom_qosh:
#     def __init__(self):
#         self.royhat = []
#     def add_food(self , nom , narx  , kaloriya):
#         taom = Taom(nom , narx  , kaloriya)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\n{food}\n'
    
# food1 = Taom_qosh()
# food1.add_food('Tuxum barak' , 40000 , 700)
# food1.add_food('Palov' , 35000 , 600)
# print(food1.info())


                                                    # 32
# class Taom:
#     def __init__(self, nom , narx  , kaloriya):
#         self.nom=  nom
#         self.narx = narx1
#         self.kaloriya = kaloriya
#     def malumot(self):
#         return f'{self.nom} , narxi {self.narx}so\'m , Kaloriya: {self.kaloriya}'
    
# class Restoran:
#     def __init__(self , nomi , manzil):    
#         self.nomi = nomi
#         self.manzil = manzil
#         self.royhat = []
#     def add_food(self ,  nom , narx  , kaloriya):
#         taom = Taom( nom , narx  , kaloriya)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} Reastoran menyusi ({self.manzil}da joylashgan): \n{food}\n'

# restoran1 = Restoran('Gavhar' , 'Urganch shaxri')
# restoran1.add_food('Palov' , 45000 , 600)
# print(restoran1.info())


                                                            # 33
# class Dastur:
#     def __init__(self,  nomi ):
#         self.nomi = nomi
#     def malumot(self):
#         return f'{self.nomi}'
    
# class Kompyuter:
#     def __init__(self):
#         self.royhat = []
#     def add_programming(self , nomi):
#         dastur = Dastur(nomi)
#         self.royhat.append(dastur)
#     def info(self):
#         programma = '\n'.join([i.malumot() for i in self.royhat])
#         return f'Kompyuterdagi dasturlar: \n{programma}\n'
    
# komp1 = Kompyuter()
# komp1.add_programming('Visual Studio Code')
# komp1.add_programming('Chrome')
# komp1.add_programming('Telegram')
# print(komp1.info())



                                                                # 34
# class Dastur:
#     def __init__(self , nomi , versiya , ishlab_chiqaruvchi):
#         self.nomi = nomi
#         self.versiya = versiya
#         self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
#     def malumot(self):
#         return f'{self.nomi} , {self.versiya} versiyada , {self.ishlab_chiqaruvchi} ishlab chiqargan'

# class Dastur_qosh:
#     def __init__(self):
#         self.royhat = []
#     def add_programming(self , nomi , versiya , ishlab_chiqaruvchi):
#         dastur = Dastur(nomi , versiya , ishlab_chiqaruvchi)
#         self.royhat.append(dastur)
#     def info(self):
#         programma = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\n{programma}\n'
    
# dastur1 = Dastur_qosh()
# dastur1.add_programming('Telegram' , 4.2 , 'Pavel Durov')
# print(dastur1.info())



                                                                    # 35
class Mijoz:
    def __init__(self, ism , familiya):
        self.ism = ism
        self.familiya = familiya