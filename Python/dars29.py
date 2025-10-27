#                 13
# numbers = [1,2,3,4,5,6,7,8,9,10,11]
# juft = list(range(2,11,2))
# toq = list(range(1,11,2))
# print('Juft sonlar : ' , juft )
# print('Toq sonlar : ' , toq)
# a = 0
# for son in range(a):
#     a = a + juft
#     for son2 in range(a):
#         a = a + toq

#             14
# numbers = []
# for i in range(1,6):
#     numbers.append(int(input(f'{i}-chi sonni kiriting : ')))
#     a = max(numbers)
#     b = min(numbers)
# print(f'{a} eng katta , {b} eng kichik')

#                 15
# harflar = ''
# matn = input('Matn kiriting : ')   
# for i in matn:
#   if i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I' or i == 'i' or i == 'O' or i == 'o' or i == 'U' or i == 'u':
#         harflar += i
# print(len(harflar))

#                 16
# text = 'Salom dunyo'
# yangi = text[::-1]
# for word in yangi:
#     print(word)

# numbers = []
# for i in range(1,6):
#     numbers.append(int(input(f'{i}-chi sonni kiriting : ')))
#     a = max(numbers)
#     b = min(numbers)
# print(f'{a} eng katta , {b} eng kichik')

son = []
for i in range(1,6):
    son.append(int(input(f'{i}-chi sonni kiriting : ')))
    a = max(son)
    b = min(son)
print(f'{a} eng katta son , {b} eng kichik son')