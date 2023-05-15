# clase llamada Math
class Math(object):

    # funcion para sumar
    def add(*data):
        total = 0
        for i in data:
            if type(i) == int:
                total += i
        return total    