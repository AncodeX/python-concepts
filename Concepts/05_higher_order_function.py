from functools import reduce

numbers = [i for i in range(1, 11)]

# Filter and Map
filter_func = list(map(lambda n: n*2, filter(lambda n: n%2 == 0, numbers)))

# Reduce
suma_list = reduce(lambda x, y: x + y, numbers)

print(suma_list)