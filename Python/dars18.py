# yosh = int(input('Yoshingizni kiriting'))
# if 0<= yosh <=7:
#     print('Siz boqcha bolasi siz')
# elif 7<= yosh <=18:
#     print('Siz maktab yoshida siz')
# elif 18<= yosh <=22:
#     print('Siz talaba siz')
# elif 23<= yosh <=60:
#     print('Siz ishlaysiz')
# elif 60<= yosh <=120:
#     print('Siz nafaqa yoshida siz')
# else:
#     print('Siz notogri son kiritdingiz')

# a = float(input('a sonini kiriting'))
# b = float(input('b sonini kiriting'))
# c = float(input('c sonini kiriting'))
# if a > b and a>c:
#     print(f"Eng katta son {a}")
# elif b>a and b>c:
#     print(f"Eng katta son {b}")
# elif c>a and c>b:
#     print(f'Eng katta son {c}')
# else:
#     print('Uchala son ham teng')


summa =  float(input('Harid summasini kiriting'))
if 0> summa >=99000:
    print('Sizda bonus yoq')
elif  summa >=150000:
    print('Sizning bonusingiz : ',summa-(summa*0.05 ))
elif 151000>= summa >=200000:
    print('Sizning bonusingiz : ', summa-(summa*0.1))
elif 201000>= summa >=300000:
    print('Sizning bonusingiz :',  summa-(summa*0.15))
elif 301000>= summa >=500000:
    print('Sizning bonusingiz :',  summa-(summa*0.3))
else:
    print('Sizda bonus yoq')