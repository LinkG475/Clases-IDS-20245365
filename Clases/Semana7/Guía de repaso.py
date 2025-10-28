"""### 1
N = int(input())
if N < 0:
    print("Negativo")
else:
    print("Positivo")

### 2
S = int(input())
if S%2 == 0:
    print(S+2)
    print(S-1)
else:
    print(S+1)
    print(S-2)

### 3
c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
c5 = float(input())
c6 = float(input())
i = (c1 + c2 + c3 + c4 + c5 + c6)/6
if i > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")

### 4
nu = int(input())
list = []
while nu > 0:
    list.append(int(input()))
    nu -= 1
print(list.count(7),list.count(5))
"""
### 5
"""N = int(input())
Pa,Pb,Pc = map(int,(input()).split())
Nc = 0
Combos = [] 
while N > 0:
    Combos.append(input())
    N -=1
for elements in Combos:
    A = Combos[Nc].count("A")
    B = Combos[Nc].count("B")
    C = Combos[Nc].count("C")
    print(A * Pa + B * Pb + C * Pc)
    Nc += 1"""

### 6
"""N = int(input())
nombres = []
while N > 0:
    nombres.append(input())
    N -= 1
O = 0
for i in nombres:
    if len(nombres[O]) <= 6:
        print("No vale la pena")
    elif len(nombres[O]) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    elif len(nombres[O]) > 6 and len(nombres[O]) < 8: 
        print("Dios no creo aguantar esta vez")
    O += 1"""

### 7
"""x,y = map(int,(input()).split())
if x < y:
    print(y)
else:
    print(x)"""

### 8
"""A = int(input())
p = 0
fila = []
while A > 0:
    fila.append(int(input()))
    A -= 1
for a in fila:
    if fila[A] > 14:
        p += 1
    A += 1
print(p) """

### 9
"""e = input()
if e == "conectado":
    print("Ola Ivan")
elif e == "desconectado":
    print("Ol..")"""

### 10
"""SL = []
N = int(input())
while N > 0:
    SL.append(int(input()))
    N -= 1
for a in SL:
    if SL[N] >= 3:
        print("Ok")
    else: 
        print("No")
    N += 1"""
