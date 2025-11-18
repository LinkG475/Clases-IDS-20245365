#Este es un docstring de modulo
# Vamos a crear varias funciones

def saludar():
    """Es una funcion que va a saludar"""
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el nombre: ")
    nombre_completo = f"{nombre.title()} {apellido.title()}"
    print(f"Hola {nombre_completo}")

saludar()

def saludar_con_param(nombre, apellido):
    """Es una funcion que va a saludar"""

    print(f"Hola {nombre.title()} {apellido.title()}")

saludar_con_param("fer", "CALVO")
saludar_con_param("Franco", "Rosales")

def describir_mascota(animal, nombre_mascota):
    """Vamos a describir mascotas."""
    print(f"Tengo un {animal}, y su nombre es {nombre_mascota.title()}.")

describir_mascota(nombre_mascota="mishito", animal="gato")
describir_mascota("perro", "Candy")
describir_mascota(
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota: ")
)

#Ejercicio de participacion
def dui_validacion(DUI):
    condiciones = 0
    ultimos = DUI[-2] + DUI[-1]
    if len(DUI) == 10:
        condiciones += 1
    if DUI.count("-") == 1:
        condiciones += 1
    if len(ultimos) == 2 and ultimos[0] == "-":
        condiciones += 1
    print(f"Cumple {condiciones} condiciones")

dui_validacion(input("Ingrese un DUI: "))
