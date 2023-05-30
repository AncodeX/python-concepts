countries = ["China", "Japon", "Corea del sur", "Colombia", "Estados Unidos", "Mexico"]
population = [1412547000, 125507000, 51439038, 51609000, 332314000, 126014024]

for c, p in zip(countries, population):
    print(f"{c}: {p}")

# Reto

nombres = ['Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Islandia', 'Estonia', 'Rusia']
nombres2 = ['Colombia', 'Venezuela', 'Ecuador', 'Mexico', 'Argentina']

*nordic_countries, es, ru = nombres
paises = [*nombres, *nombres2]

print(nordic_countries, es, ru)
print(paises)