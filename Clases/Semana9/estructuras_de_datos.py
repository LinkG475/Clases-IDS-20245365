surnames = ['Rivest','Shamir','Adleman']
for position, surname in enumerate(surnames): 
    print(position,surname) # position/correlativo

people = ['Nick','Rick','Roger','Syd']
ages = [23, 24, 23, 21]
for person, age in zip(people,ages):
    print(person, age)

names = ['Nick','Rick','Roger','Syd']
ages = [23, 24, 23, 21]
emails = ["n@", "r@", "ro@", "s@"]
phones = ["1","2","3","4"]
fruits = ["piña","manzana","uva"]
sports = ["Fut", "Bask", "Bici","P"]
for n, a, e, p, f, s in zip(names, ages, emails, phones, fruits, sports):
    print(n, a, e, p, f, s)