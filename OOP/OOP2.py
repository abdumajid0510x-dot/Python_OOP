class Mashina: 
    def __init__(self , brend , model , yil ):
        self.brend = brend
        self.model = model
        self.yili = yil
    def haqida(self):
        print(f"{self.brend} -mashina brendi , {self.model} - mashina modeli va yili: {self.yili}")
    def ishlab_chiqarish(self):
        if self.yili>2020:
            return ' Bu zamonaviy mashina'
        elif 2020>self.yili>2000:
            return 'Bu classic mashina'
        elif self.yili<2000:
            return 'Bu retro mashina'
        else:
            return 'Xatolik!!'
mashina1 = Mashina('Lambogini' , 'Urus' , 2021  )
print(mashina1.haqida(),mashina1.ishlab_chiqarish())