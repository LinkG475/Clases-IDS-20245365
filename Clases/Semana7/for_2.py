palabra = "Hola"
#print(len(palabra))
lista = [10, 11, 12, 13, 14]
#print(len(lista))
dias = ["Lunes","Martes","Miercoles",
        "Jueves","Viernes","Sabado","Domingo"]
#print(len(dias))
x = 0
for i in dias[3]:
    print(dias[3][x])
    x += 1

for i in (range(5)):
    print("Buenos días")

a = 2
for i in (range(a)):
    print(i)

VALORES = [[1,3,6],
           [2,7,4],
           [6,5,9],
           [1,10,20]]
MAYORES = []

for v in VALORES:
    print(v)
    for i in v:
        print(i)
        if i > 6:
            MAYORES.append(i)

print(MAYORES)

#dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
# Ana , Luis, Juan, Maria
horas = [[8,8,9,8,10], [7,9,10,8,7], [7,8,8,8,8], [8,8,10,7,11]]
extras1 = []
extras2 = []
total = 0
for h in horas:
    for i in h:
        if i > 8:
            extras1.append(i)
            e = i
            e -= 8
            extras2.append(e)
for x in extras2:
    total += x

print(extras1)
print(extras2)
print(f"Total de horas extras a pagar: {total}")


"""N = int(input())
nombres = []
for i in range(N):
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