presupuesto = 1000
gasto = 0

while gasto <= presupuesto:
    compra = float(input("Monto a comprar: "))
    gasto += compra
gasto -= compra
print("Ha llegado al límite del presupuesto.")
print(f"El monto gastado es de {gasto:,.2f}")

VALORES = [[1,3,6], #10
           [2,7,4], #13
           [6,5,9], #20
           [1,10,20]] #31
suma = 0
for v in VALORES:
    for i in v:
        while suma <= 45:
        #if suma <= 45:
            suma += i
            o = i
#print(suma)
suma -= o            
print(suma)