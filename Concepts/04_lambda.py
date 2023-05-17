# sintaxis

var = lambda x, y: x + y

# función lambda dentro de un función

def power(x):
    return lambda n: x ** n

cube = power(4)(3)
print(cube)
