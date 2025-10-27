                # 1
# harflar = ''
# matn = input('Matn kiriting : ')   
# for i in matn:
#   if i == 'A' or i == 'a':
#         harflar += i
# print(len(harflar))

                # 2
# text = input('Soz kiriting : ')
# print(text[::-1])

                # 3
# text = input('matn : ')
# yangi = text.upper()
# print(yangi)

                # 4
# soz = input('matn : ')
# bolaklash = soz.split()
# print(len(bolaklash))

                # 5
# a = input('matn : ')
# if a == a[::-1]:
#     print('Bu soz palindrom')
# else:
#     print('Bu soz palindrom emas'

                # 6, 7    
# matn = ['salom' , 'python', 'salom' , 'dasturlash']
# print(set(matn))

                    # 8
# unlilar = "aeiuoo'"
# yangi = ''
# matn = input('Sozni kiriting : ')
# for i in matn:
#     if i not in unlilar:
#         yangi = yangi + i 
# print(yangi)

                    # 9
# words = input('Matn :')
# bolak = words.split()
# tartib = sorted(bolak , key=str.lower())
# print(tartib)


                    # 10
# soz = input('Matn : ')
# print(soz.title())

                    # 11

# matn = input('Matn : ')
# faqat_matn = ''
# for i in matn:
#     if i.isdigit():
#         faqat_matn = faqat_matn = i
# else: print('Faqat harflardan iborat')
# print(f"Tozalangan raqamlar quyidagicha {faqat_matn}")

                        # 12
# sozlar = ''
# matn = input('Matn kiriting : ')   
# for i in matn:
#   if i == '!' or i == '?' or i == '.':
#         sozlar += i
# print(len(sozlar))

                        # 13
# matn = ['Abdumajid' , 'Murod' , 'Alijon' , 'Nizomjon']
# tartiblash = sorted(matn , key=len)
# print(tartiblash)

                        # 14
# print('salom' ,'mening' ,'ismim' ,'abdumajid' , sep='_')

                    # 15
# matn = ['salom' , 'python', 'salom' , 'dasturlash' , 'salom' , 'IT']
# print(set(matn))

                # 16
# unli = "'aioueo'"
# unlison = 0
# matn = input('Matn : ')
# undosh = 0
# for i in matn:
#     if i in unli:
#         unlisoni = unlisoni + 1
#     elif i not in unli and i!= '':
#         undosh = undosh + 1
# print(f"Unlilar soni : {unlisoni}")
# print(f"Undoshlar soni : {undosh}")

                    # 17
# matn = input('Matn : ')
# bolaklash = matn.split()
# tayyor = []
# for i in bolaklash:
#     if i.isdigit():
#         kvadrat = int(i)**2
#         tayyor.append(str(kvadrat))
#     else:
#         tayyor.append(str(i))
# javob =' '.join(tayyor)
# print(javob)
                    # 18
# matn = input('matn : ')
# bolish = {}
# for i in matn:
#     if i in bolish:
#         bolish[i] += +1 
#     else:
#         bolish[1] = 1
# eng_kopi = max(bolish)
# eng_kopi_harf = bolish[eng_kopi]
# print(f"Eng kop qtnashgan harf {eng_kopi_harf} va u {eng_kopi} marta qatnashgan")

#                     # 19
# soz = input('Matn kiriting : ')
# tartib = soz.split()
# tartiblangan = sorted(tartib , key=len)
# print(f"Eng kichik soz : {tartiblangan[0]} , eng katta soz : {tartiblangan[-1]}")

                    # 20
# matn = input('Matn : ')
# faqat_harf = ''
# faqat_son = ''
# for i in matn:
#     if i.isdigit():
#         faqat_son = faqat_son  + i
#     elif i.isalpha():
#         faqat_harf = faqat_harf + i
# print(f"Faqat sonlar : {faqat_son} , Faqat harflar : {faqat_harf}")







# for i in range(11):
#     print(i)
# i = 1
# while i<=10:
#     print(i)
#     i = i +0.5


            # 91.1
# import math
# a = int(input('a='))
# m = 1
# s = 0
# while m<=a:
#     s = s = (3*m**3 + 4*m +5)/(m**3 + math.log(m))
#     m+=1
# print(s)


                # 91.2
# import math
# b=int(input('b='))
# k=1
# p=1
# while k<=b:
#     p = p*k / (k**3+7*k+5)
#     k+=1
# print(round(p,2))

                # 91.3
# import math
# c = int(input('c='))
# d = int(input('d='))
# s=0
# m=1



            # 92.1
# import math
# x = int(input('x='))
# s = 0
# a=1
# while a<=x:
#     s=s+(a**2 + a*2)/(a**3 + a*math.cos(a)**2+1)
#     a+=1
# print(round(s,2))


            # 92.2
# import math
# y = int(input('y='))
# p=1
# i=1
# while i<=y:
#     p = p * (i**2+1)/((i**3+2)**(1/i))
#     i+=1
# print(round(p ,2))


            # 92.3
# import math
# a = int(input('a='))
# b = int(input('b='))
# s = 0
# p=1
# k=1
# i=1
# for i in range(1 , a+1):
#     p=1
#     for k in range(1,b+1):
#         p = p*(math.log((k**i+k**(1/i))/(k**3 + i**(1/k))))
#     s=s+p
# print(round(s,2))

                                                                                             # 25.06.25
                            # 93.1
# import math
# x = int(input('x='))
# k=1
# s = 0
# while k<=x:
#     s=s+(k**2+math.sin(k)+5)/((k**7+1)**(1/5))
#     k+=1
# print(round(s,2))

                        # 93.2
# import math
# y = int(input('y='))
# n=1
# p=1
# while n<=y:
#     p=p*((n+n**(1/2))/(n-((n+1)**(1/5))))
#     n+=1
# print(round(p,2))

                    # 93.3
# import math
# a=int(input('a='))
# b=int(input('b='))
# k=1
# p=1
# i=1
# s=0
# for i in range(1,a+1):
#     p=1
#     for i in range(1,b+1):
#           p=p*((i**2+(k**2)**(1/i))/(math.sin(i)+math.cos(k))**i)
#     s=s+p
# print(round(s,2))


                # 94.1
# import math
# x = int(input('x='))
# a=1
# s=0
# while a<=x:
#     s=s+(2*a+math.cos(a))**2
#     a+=1
# print(round(s,2))


                    # 94.2
# import math
# y=int(input('y='))
# a=1
# p=1
# while a<=y:
#     p=p*((a+6)/(((a**2)+2)**(1/2)))
#     a+=1
# print(round(p,2))


                    # 94.3
# import math
# c=int(input('c='))
# d=int(input('d='))
# k=1
# y=1
# s=0
# p=1
# for i in range(c,c+1):
#     p=1
#     for i in range(d,d+1):
#         p=p*((k**2+y)/((k**2+y**2)**(1/2)))
#     s=s+p
# print(round(s,2))
    

                    # 95.1
# import math
# x=int(input('x='))
# s=0
# i=1
# while i<=x:
#     s=s+((i**4+i**2+3)/(i+math.exp(1)**i)**(1/2))
#     i+=1
# print(round(s,2))

                # 95.2
# import math
# y=int(input('y='))
# k=1
# p=1
# while k<=y:
#     p=p+((k+1)/(k**3 + 5*k))
#     k+=1
# print(round(p,2))


                    # 95.3
# import math
# c=int(input('c='))
# d=int(input('d='))
# m=1
# n=1
# s=0
# p=1
# for m in range(1,c+1):
#     p=1
#     for n in range(1,d+1):
#         p=p*((((abs(m**n-n**m))/(m**n+n**m)))**(1/2))
#     s=s+p
# print(round(s,2))

                    # 96.1
# import math
# c=int(input('c='))
# d=int(input('d='))
# m=1
# n=1
# s=0
# for n in range(1,c+1):
#     s=0
#     for m in range(1,d+1):
#         s=s+(((-1)**m * (math.log(m+5))/(m**(n+3)+n*m)))
#     p=p*s
# print(round(p,2))


                                                                            # 27.06.2025
                                #  97.1
# x=int(input('x='))
# n=1
# s=0
# while n<=x:
#     s=s+(1/(5-17*n + n**3))
#     n+=1
# print(round(s,2))


                        #  97.2
# y=int(input('y='))
# m=1
# p=1
# while m<=y:
#     p=p*(((abs(m-5)+1)**(1/2))/(m**2+4*m-1))
#     m+=1
# print(round(p,2))



                # 97.3
# import math
# c=int(input('c='))
# d=int(input('d='))
# i=1
# k=1
# s=0
# p=1
# for i in range(1,c+1):
#     p=1
#     for k in range(1,d+1):
#         s=s+(-1**i)*(abs(math.sin(k)+math.exp(1)))**(1/7)/(2*(abs(4*i**3 - k**4)))
#     p=p*s
# print(round(p,2))


                            # 98.1
# import math
# x=int(input('X='))
# s=0
# a=1
# while a<=1:
#     s=s+((4*a+6*(math.log(a)))/(a**2 + a))
#     a+=1
# print(round(s,2))

                    # 98.2
# import math
# y=int(input('y='))
# a=1
# p=1
# while a<=y:
#     p=p*((abs(a-6 * math.cos(a)))/(a**2+a**(math.log(a))))
#     a+=1
# print(round(p,2))


                        # 98.3
# import math
# c=int(input('c='))
# d=int(input('d='))
# a=1
# k=1
# s=0
# p=1
# for a in range(1,c+1):
#     p=1
#     x=1
#     y=1
#     for k in range(1,d+1):
#         p=p*((a*k + x)/ (k**2 + y**2))
#     s=s+p
# print(round(s,2))



                # 101

# numbers = []
# n = int(input('nechta son : '))
# for i in range(1,n+1):
#     son = int(input(f'{i}-son : '))
#     numbers.append(son)
# orta_a = sum(numbers) / len(numbers)
# yangi_m = []
# for numbers in numbers:
#     if numbers<orta_a:
#         yangi_m.append(numbers)
# print(sum(yangi_m) / len(yangi_m))


                # 102
# massiv = []
# n = int(input('nechta son : '))
# for i in range(1,n+1):
#     son = int(input(f'{i}-son : '))
#     massiv.append(son)
# a = int(input('a = '))-1
# b = int(input('b = '))-1
# yangi = []
# minimum = min(massiv)
# for i in range(len(massiv)):
#     if a<=i<=b:
#         yangi.append(round(massiv[i] / minimum , 1))
#     else:
#         yangi.append(i)
# print(yangi)
        

                # 103
# numbers = []
# n = int(input('nechta son : '))
# for i in range(1,n+1):
#     son = int(input(f'{i}-son : '))
#     numbers.append(son)
# k = int(input('k = '))
# i = int(input('i = '))
# massiv = numbers[k-1:i]
# ortacha_q = sum(massiv) / len(massiv)
# print(round(ortacha_q , 1))


            # 105
# massiv = []
# n = int(input('nechta son : '))
# for i in range(1,n+1):
#     son = int(input(f'{i}-son : '))
#     massiv.append(son)
# a = int(input('a = '))
# b = int(input('b = '))
# del massiv[a-1:b]
# yangi = sum(massiv)/ len(massiv)
# print(yangi)

# numbers = []
# n = int(input('nechta son : '))
# for i in range(1,n+1):
#     son = int(input(f'{i}-son : '))
#     numbers.append(son)
# summa = 0 
# for i in range(len(numbers)):
#     kvadrat = numbers[i] **2
#     summa = summa + kvadrat
# print(summa)

massiv = []
n = int(input('nechta son : '))
for i in range(1,n+1):
    son = int(input(f'{i}-son : '))
    massiv.append(son)
a = int(input('a = '))-1
b = int(input('b = '))-1
yangi = []
maximum = max(massiv)
for i in range(len(massiv)):
    if a<=i<=b:
        yangi.append(round(massiv[i] / maximum , 1))
    else:
        yangi.append(i)
print(yangi)