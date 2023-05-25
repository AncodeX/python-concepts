lista = []
lista = ["Banana", "Rocket", 2, True, 2.3]
print(lista[0], lista[int(len(lista)/2)], lista[-1])

mixed_data_types = ["Daniel", 19, 1.70, "soltero", "calle 8"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])
it_companies[2] = "Samsung"
print(it_companies)
it_companies.append("Microsoft")
it_companies.insert(int(len(it_companies)/2), "OpenAI")
print(it_companies)

company = "Google"
it_companies = list(map(lambda c: c.upper() if c == company else c, it_companies))

print(list(map(lambda x: "#" + x, it_companies)))

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)