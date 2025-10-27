# lugat = {'ball':'top' , 'phone':'telefon' , 'table':'stol'}
# print(lugat.items())
# name = input('Soz kiriting : ')
# print(lugat[name])

# lugat = {'ball':'top' , 'phone':'telefon' , 'table':'stol'}
# n = int(input('Nechda soz tarjima qilish kerak '))
# for i in range(1,n):
#     name = input(f'{i}-sozni kiriting : ')
#     print(lugat.get(name , 'Bu soz bazadan topilmadi'))

lugat = {'ball':'top' , 'phone':'telefon' , 'table':'stol'}
a = input('Kalit sozni kiriting : ')
b = input('Qiymatni kiritin : ')
lugat[a] = [b]
print(lugat.items())