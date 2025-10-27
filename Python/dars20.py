# name = input('Ism kiriting : ')
# if name.startswith('a' or'i' or'o'or'u' or'e' or 'o\''):
#     print('Siz unli harf bilan boshlanadigan ism kiritingiz')
# else:
#     print('Siz undosh hatf bilan boshlanadigan ism kiritingiz')

# email = input('Emailingizni kiriting : ')
# if '@' in email and email.endswith('.com'):
#     print('Email tastiqlandi')
# else:
#     print('Siz xato email kiritingiz')

email = input('Emailingizni kiriting : ')
if '@' in email and email.endswith('.com'):
    print('Email tastiqlandi')
elif '@' not in email and '.com' not in email:
    print('Siz @ va .com yozmadingiz')
elif '@' not in email:
    print('Siz @ yozmadingiz')
elif '.com' not in email:
    print('Siz .com yozmadingiz')

else:
    print('Siz xato email kiritingiz')