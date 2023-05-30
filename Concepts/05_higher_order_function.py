from functools import reduce

# Funcion como parametro

def sum_numbers(ns):
    return sum(ns)

def higher_order_function(f, lst):
    summation = f(lst)

    return summation

result = higher_order_function(sum_numbers, [2, 3, 4, 5])
print(result)

# Funcion como valor de retorno

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def mult(x, y):
    return x * y


def operation(op):
    if op == "suma":
        return suma
    elif op == "resta":
        return resta
    elif op == "mult":
        return mult
    
result = operation("mult")(4, 5)
print(result)

# Clousure

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

result = add_ten()(5)
print(result)

# map

names = ["daniel", "michaell", "sebastian", "santiago"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

names_upper = list(map(lambda n: n.capitalize(), names))
print(names_upper)

# filter

names_filter = list(filter(lambda c: True if c.endswith("l") else False, names))
print(names_filter)

# reduce

total = reduce(lambda a,b: a+b, numbers)
print(total)