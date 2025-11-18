# Configuracion inicial
alumnos = 0
lista_alumnos = []



print("Bienvenido a nuestro sistema de control de Alumnos.")

menu_activo = True

while menu_activo:
    opcion = input("Elija la opcion (1: Ingresar alumno, 2: Consultar, 3: Modificar, 4: Borrar alumno, 5: Salir): ")
    if opcion == "5":
        menu_activo = False
    elif opcion == "1":
        alumno = input("Nombre del alumno a agregar: ")
        lista_alumnos.append(alumno)
    elif opcion == "2":
        print(lista_alumnos)
        for i in lista_alumnos:
            print(i)
    elif opcion == "3":
        n = int(input("Ingrese la posición del alumno a modificar: "))
        lista_alumnos[n-1] = input("Ingrese el nuevo nombre del alumno: ")
    elif opcion == "4":
        """borrar = input("Ingrese nombre de alumno a borrar: ")
        lista_alumnos.remove(borrar)"""
        # Opción 2
        borrado = lista_alumnos.pop(int(input("Ingrese el número del alumno a popear (1-4): "))-1)        
        print(f"Usted ha popeado a {borrado}.")
    else:
        print("La elección no es valida.")
        
print("Gracias por utilizar nuestro Sistema.")