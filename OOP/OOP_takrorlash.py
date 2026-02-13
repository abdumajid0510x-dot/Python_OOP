# class Kasalxona:
#     def __init__(self, nomi):
#         self.nomi = nomi
#     def doktorga_yozilish(self):
#         doktor_royhat = {
#             1:'Aliev Ali',
#             2:'Valiev Vali',
#             3:'Xasanboyev Golibjon',
#             4:'Shokirov Shokir' 
#         }
#         print(f'{self.nomi}dagi shofokorlar royhati {doktor_royhat}')
        
#         yozilish  = int(input('Qaysi doktorga yozilmoqchisiz? tartib raqam bn kiriting: '))
#         ali= 0
#         vali = 0
#         golib = 0
#         shokir = 0

#         if yozilish == 1:
#             ali +=1
#             return f'Siz Aliyev Ali navbatiga yozildingiz va bu doktor navbatida turganlar soni {ali}.' 
#         elif yozilish == 2:
#             vali +=1
#             return f'Siz Valiyev Vali navbatiga yozildingiz va bu doktor navbatida turganlar soni {vali}.'
#         elif yozilish == 3:
#             golib +=1
#             return f'Siz Xasanboyev Golibjon navbatiga yozildingiz va bu doktor navbatida turganlar soni {golib}.'
#         elif yozilish == 4:
#             shokir +=1
#             return f'Siz Shokirov Shokir navbatiga yozildingiz va bu doktor navbatida turganlar soni {shokir}.'
#         else:
#             return f'Iltimos tartib raqam bilan kiriting!'
        
# balnitsa1 = Kasalxona('Tuman kasalxonasi')
# while True:
#     print(balnitsa1.doktorga_yozilish())




# class Doktor:
#     def __init__(self , name):
#         self.name  = name
#         self.bemorlar = []
#     def add_bemor(self , bemor_name):
#         self.bemorlar.append(bemor_name)
#     def show_bemor(self):
#         return self.bemorlar
#     def count_bemor(self):
#         return len(self.bemorlar)
    
# class Shifoxona:
#     def __init__(self , shifo_name):
#         self.shifo_name = shifo_name
#         self.doktorlar = []
#     def add_doktor(self , doc_name):
#         self.doktorlar.append(doc_name)

#     def show_doktors(self):
#         for index , ism in enumerate(self.doktorlar):
#             print(f'{index}.{ism}')

# class Bemor:
#     def __init__(self , name):
#         self.name = name
#     def choose_doktor(self , doktor):
#         doktor.add_bemor(self.name)
#         print(f'{self.name} {doktor.name}ga navbatga yozildi.')
#         print(f'Navbatda: {doktor.count_bemor()} nafar bemor va ular {doktor.show_bemor()}.')
    
# bemor1 = Bemor('Shomurod')
# bemor2 = Bemor('Shokir')
# bemor3 = Bemor('Sipsagul')
# doktor1 = Doktor('Dr. Abduvaid')
# doktor2 = Doktor('Dr. Ali')
# shifoxona1 = Shifoxona('Tuman shifoxonasi')
# shifoxona1.add_doktor(doktor1)
# shifoxona1.add_doktor(doktor2)
# bemor1.choose_doktor(doktor1)


class Avtomobil:
    def __init__(self , avto_nomi , avto_narx):
        self.avto_nomi = avto_nomi
        self.avto_narx = avto_narx
        self.mijozlar = []
    def add_mijoz(self , mijoz_name):
            self.mijozlar.append(mijoz_name)
    def narx_hisobla(self):
        return f'{self.avto_narx / 2}'
    def mijozlarni_korsatish(self):
        return self.mijozlar
    def navbat_mijozlar(self):
        return len(self.mijozlar)
    
class Avtosalon:
    def __init__(self , salon_name):
        self.salon.name = salon_name
        self.avtolar = []
    def add_avtomobil(self , avto_name):
        self.avtolar.append(avto_name)
    def avtolarni_korsatish(self): 
        for joylashuv , model in enumerate(self.avtolar):
            print(f'{joylashuv}.{model}')

class Haridor:
    def __init__(self, mijoz_ism):
        self.mijoz_ism = mijoz_ism
    def avto_tanlash(self , mashina):
        mashina.add_mijoz(self.mijoz_ism)
        print(f'{self.mijoz_ism} {mashina.avto_nomi} ga {self.narx_hisobla()}som tolab navbaga yozildi')
        print(f'Navbatda: {mashina.count_bemor()} nafar haridor bor.')


haridor1 = Haridor('Shokir')
haridor2 = Haridor('Ali')
avto1 = Avtomobil('Jentra')
avto2 =Avtomobil('Cobalt')
avtosalon1 = Avtosalon('Pitnak bozor')
avtosalon1.add_avtomobil(avto1)
avtosalon1.add_avtomobil(avto2)
haridor1.avto_tanlash(avto1)