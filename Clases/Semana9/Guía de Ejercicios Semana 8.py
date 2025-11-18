# Cafetería ESEN Brew
clientes = {} # "codigo": ["nombre", "correo", "telefono"]
productos = {} # "codigo": ["nombre", "categoria", "precio"]
pedidos = {} # "codigocliente": "codigoproducto"
while True:
    opcion = input("Elija que opción desea: (1: Mostrar productos, 2: Agregar productos, 3: Registrar nuevo cliente, 4: Mostrar clientes, 5: Registrar pedido, 6: Mostrar pedidos del dia, 7: Mostrar categorias disponibles, 8: Salir): ")
    if opcion == "1":
        if len(productos) == 0:
            print("No hay productos disponibles.")
        else:
            print(productos)
    elif opcion == "2":
        codigou = input("Introduzca el código de producto: ")
        nombrepr = input("Introduzca el nombre del producto: ")
        categoria = input("Introduzca la categoría del producto: ")
        precio = float(input("Introduzca el precio del producto: "))
        productos[codigou]= [nombrepr, categoria, precio]
    elif opcion == "3":
        codigo = input("Introduzca el código de cliente: ")
        nombrec = input("Introduzca el nombre del cliente: ")
        correo = input("Introduzca el correo del cliente: ")
        telefono = input("Introduzca el número de telefono del cliente: ")
        clientes[codigo]= [nombrec, correo, telefono]
    elif opcion == "4":
        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:
            print(clientes)
    elif opcion == "5":
        codigosproductos = []        
        iteraciones = 0
        if len(productos) != 0 and len(clientes) != 0:
            cp = int(input("Cuantos productos desea pedir?: "))
            while cp >= 1:
                codigoproducto = input("Introduzca el código de producto: ")
                for cpr in productos.keys():
                    if codigoproducto == cpr:
                        codigosproductos.append(codigoproducto)
                        cp -= 1                    
                        break       
                    else: 
                        iteraciones += 1         
                if iteraciones == len(productos.keys()):
                    print("Ese codigo de producto no existe.")
                    iteraciones = 0
        elif len(productos) == 0:
            print("No hay productos disponibles.")          
        if len(productos) != 0 and len(clientes) != 0:    
            iteraciones = 0
            while True:
                codigocliente = input("Introduzca el código de cliente: ")
                for cc in clientes.keys():
                    if codigocliente == cc:
                        pedidos[cc] = codigosproductos
                        break
                    else: 
                        iteraciones += 1
                if iteraciones == len(clientes.keys()):
                    print("Ese codigo de cliente no existe.")
                    iteraciones = 0
                else:
                    break
        elif len(clientes) == 0:
            print("No hay clientes registrados.")
    elif opcion == "6":
        total = 0
        for k, p in productos.items():
            if k in pedidos.keys(): 
                total += p[2]
        if total != 0: 
            print(f"Los pedidos de hoy son: {pedidos}, y el total acumulado es: ${total:.2f}")
        else:
            print("No hay pedidos este día.")
    elif opcion == "7":
        if len(productos) != 0:
            for categoria in productos.values():
                    categorias = {categoria[1]}
            print(f"Las categorías disponibles son: {categorias}")
        else:
            print("No hay categorías registradas.")
    elif opcion == "8":
        break