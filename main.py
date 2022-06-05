import math

i = int(input())

def oblicz_pole(figura):
    l = len(figura)
    
    if l == 1:
        return math.pi * figura[0]**2
    
    if l == 2:
        return figura[0] * figura[1]
    
    if l == 3:
        s = (figura[0] + figura[1] + figura[2]) / 2
        return (s * (s - figura[0]) * (s - figura[1]) * (s - figura[2])) ** 0.5
    
    if l >= 4:
        return 'N/D'

suma_pol = 0

for n in range(i):
    x = list(map(float, input().split()))
    pole = oblicz_pole(x) 
    if pole == 'N/D':
        sum = 'N/D'
        break
    suma_pol = suma_pol + oblicz_pole(x)

if sum != 'N/D':
    print(format(suma_pol, ".2f"))
else:
    print('Błąd: można podać maksymalnie 3 liczby')
