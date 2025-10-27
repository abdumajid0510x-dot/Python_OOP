# a = int(input('Son kiriting : '))
# if a%2==0:
#     if a%3 == 0:
#         print('Bu son juft hamda 3 ga qoldiqsiz bolinadi')
#     else: print('Bu son juft lekin 3 ga qoldiqsiz bolinmaydi')
# else:
#     print("Bu toq son")
    
# a = int(input('Son kiriting : '))
# if a > 0:
#     if a%5 == 0:
#         print('Musbat va 5 karra!!!!')
#     else: print('Musbat lekin 5 ga karrali emas')
# else:
#     print("Bu son musbat emas")

# login = input('Login kiriting : ')
# if login == 'abdumajid.com':
#     parol = input('Parol kiriting : ')
#     if parol == 'abdu':
#         print('Togri')
#     else:
#         print('notogri')
# else:
#     print('Xatolik')

a = input('Telefon raqamingizni kiriting : ')
if a.startswith('+998'):
    if a.startswith('+9989'):
        print('togri')
    else:
        print('notogri')
else:
    print('Xatolik')
