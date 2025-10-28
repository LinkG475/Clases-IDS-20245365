datos = [1,2,"tres",["lunes","martes","miercoles"]]
print(datos[3][2][3])
print(datos[-1][-1][3])

numeros = ["uno","dos","tres"]
print(numeros)
numeros = numeros + ["cuatro","cinco","seis"]
print(numeros)
print(len(numeros))
numeros[2] = "trois"
print(numeros)
numeros.append(input("Escriba el siguiente numero: "))
print(numeros)
numeros.insert(2, input("Einender nummer: "))
print(numeros)