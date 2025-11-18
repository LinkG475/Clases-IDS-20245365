# Un pequeño sistema de registro de alumnos

# Configuracion inicial
alumnos = 0
lista_alumnos = []
cantidad = int(input("Cuantos alumnos vamos a ingresar: "))
"""alumno = input("Digite nombre del pajarito: ")
lista_alumnos.append(alumno)
alumno = input("Digite nombre del pajarito: ")
lista_alumnos.append(alumno)
alumno = input("Digite nombre del pajarito: ")
lista_alumnos.append(alumno)"""

for i in range(cantidad):
    alumno = input("Digite nombre del pajarito: ")
    lista_alumnos.append(alumno)

print( lista_alumnos)

alumnos = len(lista_alumnos)
print(alumnos)