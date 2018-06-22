from math import sqrt as raiz
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(a)
menor = a[0]
maior = 0
soma = 0
var = 0
pm = 0
pma = 0
for i in range(25):
    if a[i] < menor:
        menor = a[i]
        pm = i
    if a[i] > maior:
        maior = a[i]
        pma = i
    soma+=a[i]

media = soma/25
for i in range(25):
    var+=(a[i]-media)**2
var/=25
dp = raiz(var)
print(menor)
print(maior)
print(pm)
print(pma)
print(media)
print(dp)
