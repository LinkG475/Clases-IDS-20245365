#Ejercicio de participacion 6/11/2025 German Suazo
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
