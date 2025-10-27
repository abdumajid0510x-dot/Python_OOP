'''names=[]
names.append('Alijon')
names.append('Abdumajid')
names.append('Shahriyor')
names.append('Murod')
tartiblash= sorted(names , key=len)
print(tartiblash)'''

'''numbers=str(list(range(1,100,2)))
tartib= sorted(numbers , key = len)
print(tartib)'''

'''ism=input('Siz menga ismingizni teskari yozing men togirlab yozib beraman :')
print('Sizning togirlanganismingiz : ' , ism[::-1].title())'''

'''Lists = list(range(11 , 100))
print(Lists[0] + Lists[10]) '''          


'''a = int(input('a sonini kiriting'))
b = int(input('b sonini kiriting'))
javob = (a**(2+a/b))/(a+b)**(1/2)
print(javob)'''


'''a = int(input('a sonini kiriting :'))
b = int(input('b sonini kiriting :'))
d = int(input('d sonini kiriting :'))
javob = (a+b)/(a**2+b/d)+(a**3+b**(1/2))**(1/2)
print(javob)'''


a = int(input('a sonini kiriting :'))
b = int(input('b sonini kiriting :'))
javob = (a**(b**(1/2))+b**(a**(1/2)))**(1/2) 
print(javob)
