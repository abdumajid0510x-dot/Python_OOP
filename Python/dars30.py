# ism = (input('Ismingizni kiriting : '))
# togri = ism.strip(), ism.title()
# print(togri)

# email = (input('Elektron pochtangizni kiriting : '))
# if '@' and '.' and 'com' in email:
#      print('True')
# else:
#      print('False')

raqam = input('Telefon raqamingizni kiriting : ' )
if len(raqam) ==12:
    print( f"+998 ({raqam[3:5]}) {raqam[5:8]}-{raqam[8:10]}-{raqam[10:12]}")
elif len(raqam) == 9:
    print(f"+998 ({raqam[0:2]})-{raqam[2:5]}-{raqam[5:7]}-{raqam[7:9]}")
else:
    print('Xatolik!!!')




# matn = 'This is an important message'
# if 'important' in matn:
#     print('True')
# else:
#     print('False')

# parol = int and str(input('Parol kiriting : '))
# if parol.lower() or parol.upper() or parol.digit():
#     print('True')
# else:
#     print('False')

# matn = (input('Kitob nomini kiriting : '))
# togri = matn.title()
# print(togri)

