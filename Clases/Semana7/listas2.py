nombres = ["Ana","Antonio","Ana","Jose"]
r_a = 0
print(nombres.count("Maria"))
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)

r_a = 0
a = 0
for elements in nombres:
    r_a = r_a + nombres[a].lower().count("a")
    a += 1
print(r_a)

print(nombres.index("Ana",nombres.index("Ana")+1))