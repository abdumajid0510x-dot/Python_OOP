import math
a = float(input('a = '))
b = float(input('b = '))
# print((x=y)/((y**2)+abs((y**2+2)x+(x**3)/5))+math.exp(1)math.pow(y+2))
ildiz = a**(1/5)
ildizk = (b*((a+b)/(2*b+a*b)))**(1/4)
qovs = (a**2 + b**2 + 2)
T = ildiz + ildizk * qovs
print(round(T,2))