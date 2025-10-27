#name = 'Alijon'
#print(name.isdigit())
#numbers = '1234'
#print(numbers.isalpha())
#sport = 'Foodball'
#print('o' in sport)
#print('t' not in sport)

'''name = 'Abdumajid'
age = '14'
malumot = 'Mening ismim {} va men {} yoshdaman'
print(malumot.format(name , age))'''

'''tuman = 'Tuproqqala'
ism = 'Abdumajid'
yosh = 14
maktab = '2-son'
print('Men %s tumanida yashayman mening ismim %s va %d yoshdaman va %s maktabida oqiyman' %(tuman,ism,yosh,maktab))'''

'''viloyat = 'Xorazm'
tuman = 'Tupraqqala'
ism = 'Abdumajid'
yosh = 14 
soha = 'IT'
kelajak = 'dasturchi'
malumot = f"Men {viloyat} viloyati {tuman} tumanida yashayman mening ismim {ism} men {yosh} man va men {soha} sohasiga qiziqaman
kelajakda {kelajak} bolmoqchi man "
print(malumot)'''

'''viloyat = 'Xorazm'
tuman = 'Tupraqqala'
ism = 'Abdumajid'
yosh = 14 
soha = 'IT'
kelajak = 'dasturchi'
malumot =("Men %s viloyati %s tumanida yashayman mening ismim %s men %d yoshda man va men %s sohasiga qiziqaman kelajakda %s bolmoqchi man"  %(viloyat , tuman , ism , yosh , soha , kelajak))
print(malumot)'''

viloyat = 'Xorazm'
tuman = 'Tupraqqala'
ism = 'Abdumajid'
yosh = 14 
soha = 'IT'
kelajak = 'dasturchi'
malumot ="Men {} viloyati {} tumanida yashayman mening ismim {} men {} yoshda man va men {} sohasiga qiziqaman kelajakda {} bolmoqchi man"  
print(malumot.format(viloyat,tuman,ism,yosh,soha,kelajak))