### Ejercicio 1
# Captura de cantidades 
"""Enero = int(input("Digite las cantidades producidas en Enero:"))
Febrero = int(input("Digite las cantidades producidas en febrero:"))
Marzo = int(input("Digite las cantidades producidas en marzo:"))

#print(Enero*1.25 + Febrero*1.38 + Marzo*1.14)
costo = Enero*1.25 + Febrero*1.38 + Marzo*1.14
print(costo)
print(f"Las cantidades de enero, febrero, y marzo son:")
print(f"{Enero}, {Febrero} y {Marzo} con un costo")
print(f"de ${costo:.2f}")"""

### Ejercicio 2
"""DIAS = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
LU = int(input("Lunes: "))
DIAS[0] = LU
print(DIAS) 
MA = int(input("Martes: "))
DIAS[1] = MA
print(DIAS) 
MI = int(input("Miercoles: "))
DIAS[2] = MI
print(DIAS) 
JU = int(input("Jueves: "))
DIAS[3] = JU
print(DIAS) 
VI = int(input("Viernes: "))
DIAS[4] = VI
print(DIAS) 
print(f"La producción de la semana fue {LU+MA+MI+JU+VI}")
print("La producción de la semana fue" , LU+MA+MI+JU+VI)"""

### Ejercicio 3
"""frutas = [1,2,3,4,5,6]
uno = input("Primer niño: ")
frutas[0] = uno
print(frutas)
dos = input("Segundo niño: ")
frutas[1] = dos
print(frutas)
tres = input("Tercer niño: ")
frutas[2] = tres
print(frutas)
cuatro = input("Cuarto niño: ")
frutas[3] = cuatro
print(frutas)
cinco = input("Quinto niño: ")
frutas[4] = cinco
print(frutas)
seis = input("Sexto niño: ")
frutas[5] = seis
print(frutas)"""

### Ejercicio 4
"""alumnos = ("Diego","Franquito","Calvito","Aby","Alvin","Medranito","Genesis")
ninio = int(input("Ingrese el orden del niño que desa saber (1-7): "))
print(f"El alumno que ingresó como numero {ninio} es {alumnos[ninio-1]}")
"""

### Ejercicio 5
"""nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")

correo1 = nombre.lower()+"."+apellido.lower()+"@ISND.com"
correo2 = nombre[0].lower()+apellido.lower()+"@ISND.com"
print(f"Propuesta 1: {correo1}")
print(f"Propuesta 2: {correo2}")"""

### Ejercicio 6
"""salario = input("Ingrese salario: ")
print(salario.count("$") == 1)
print("$" in salario[0]) #forma 2
print(salario[0] =="$") #forma 1

### Ejercicio 7
palabra = input("Ingrese contraseña:") #DFGUPCCBJKAJ"
print(palabra[0::3])""" 


### Tienda Semanal 
#Solución 1
dias = ["lunes","martes","miercoles","jueves","viernes"]
lunes = int(input())
martes = int(input())
miercoles = int(input())
jueves = int(input())
viernes = int(input())
dias[0] = lunes
dias[1] = martes
dias[2] = miercoles
dias[3] = jueves
dias[4] = viernes
print(f"El día LUNES se vendieron {dias[0]} productos")
print(f"El día MARTES se vendieron {dias[1]} productos")
print(f"El día MIERCOLES se vendieron {dias[2]} productos")
print(f"El día JUEVES se vendieron {dias[3]} productos")
print(f"El día VIERNES se vendieron {dias[4]} productos")

#Solución 2
lunes = int(input())
martes = int(input())
miercoles = int(input())
jueves = int(input())
viernes = int(input())
print("El día LUNES se vendieron", lunes, "productos")
print("El día MARTES se vendieron", martes ,"productos")
print("El día MIERCOLES se vendieron", miercoles ,"productos")
print("El día JUEVES se vendieron", jueves, "productos")
print("El día VIERNES se vendieron", viernes, "productos")