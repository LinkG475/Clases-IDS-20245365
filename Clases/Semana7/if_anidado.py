tipo = input()
if tipo.lower() == "local":
    montol = float(input())
    if montol > 100:
        impuesto = "7%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")
    elif montol > 75:
        impuesto = "5%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")
    elif montol <= 75:
        impuesto = "0%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")

elif tipo.lower() == "internacional":
    montoi = float(input())
    if montoi > 100:
        impuesto = "12%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")
    elif montoi > 75:
        impuesto = "9%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")
    else:
        impuesto = "0%"
        print(f"Impuesto {tipo.lower()}: {impuesto}")
else:
    print("Ese tipo no existe")
#####
monto = float(input("Digite el monto: "))
tipo = input()
if tipo.lower() == "local":
    if monto > 100:
        impuesto = 0.07
    else: 
        if monto > 75:
            impuesto = 0.05
        else:
            impuesto = 0
elif tipo.lower() == "internacional":
    if monto > 100:
        impuesto = 0.12
    else: 
        if monto > 75:
            impuesto = 0.09
        else:
            impuesto = 0

if tipo.lower() == "local" or tipo.lower() == "internacional":
    print(f"El tipo {tipo.lower()} con monto {monto:,.2f}")
    print(f"paga un impuesto de {monto*impuesto:,.2f}")
else:
    print("Ese tipo no existe")