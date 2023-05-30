from functools import reduce
from lista_paises import countries
"""
    Map: En mi perspectiva de programación un mapa tiene la misma funcionalidad de un for recorrera una lista y podremos manipular cada iterable y devolvera este
    Filter: Lo mismo que Map pero en vez de devolver el iterable nos devolvera un True o False
    Reduce: Nos retornara un solo valor
"""

#countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lower_countries = list(map(lambda c: c.lower(), countries))
# print(lower_countries)

# square_numbers = list(map(lambda n: n ** 2, numbers))
# print(square_numbers)

# upper_names = list(map(lambda n: n.upper(), names))
# print(upper_names)

# countries_land = list(filter(lambda c: c.endswith("land"), countries))
# print(countries_land)

# countries_land = list(filter(lambda c: len(c) == 6, countries))
# print(countries_land)

# countries_land = list(filter(lambda c: len(c) >= 6, countries))
# print(countries_land)

# countries_land = list(filter(lambda c: c.startswith("E"), countries))
# print(countries_land)

# suma_total = reduce(lambda a, b: a +b, numbers)
# print(suma_total)

# conct_countries = reduce(lambda x, y: x + ", " + y, countries)
# print(conct_countries + " are north European countries")

def categorize_country(pattern):
    list_filter = list(filter(lambda c: c.endswith(pattern), countries))
    return list_filter

print(categorize_country("ia"))