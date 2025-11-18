semana = {}
semana["uno"] = "lunes"
semana["dos"] = "martes"
semana["tres"] = "miercoles"
semana["cuatro"] = "jueves"
semana["cinco"] = "viernes"
print(semana)
print(semana.values())
print(len(semana.values()))
for k, v in semana.items():
    print(f"El dia {k} de la semana es {v}")


pr = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
pe = {1:"x", 4: "y", 3:"z"}
total = 0
t = []
print(pr.items())
for k, p in pr.items():
    if k in pe.keys(): 
        t.append(p[2])
        total += p[2]
print(t)
print(total)