# harflar = ''
# matn = input('Matn kiriting : ')   
# for i in matn:
#     if i == 'A' or i == 'a' or i == 'I' or i == 'i' or i == 'E' or i == 'e' or i == 'O' or i == 'o' or i == 'U' or i == 'u':
#         harflar += i
# print(len(harflar))

gap = ''
matn = input('Matn kiriting : ')   
for i in matn:
    if i == 'a' or i == 'A':
        gap += i
print(len(gap)) 
