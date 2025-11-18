birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4" 
}

birthdays["Carol"] ="Abr 21"
birthdays["Fer"] ="Mar 3"
print(birthdays)
print(birthdays["Fer"])

for persona, fecha in birthdays.items():
    print(f"El cumpleaños de {persona} es en {fecha}")

del birthdays["Bob"]
print(birthdays)