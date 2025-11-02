# Voy a iniciar mi variable en True
ejecucion = True

while ejecucion == True:
    opcion = input("Estamos ejecutando el mendu? Y/N:")
    if opcion.lower() == "n":
        ejecucion = False
    elif opcion.lower() == "y":
        ejecucion = True
        print("Ok, continuemos.")
    else: 
        print("La opcion elegida no es valida.")

print("Gracias por utilizar nuestro sistema!!!")
