"""
Reto #4: ÁREA DE UN POLÍGONO

    Crea una única función (importante que sólo sea una) que sea capaz
    de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""

def poligono(figura:str):
    try:
        if figura == "triangulo":
            base = int(input("Base del triangulo: "))
            altura = int(input("Altura del triangulo: "))

            area = (base*altura)/2

            return area
        elif figura == "cuadrado":
            lado = int(input("Lado del cuadrado: "))

            area = lado*lado

            return area
        elif figura == "rectangulo":
            largo = int(input("Largo del rectangulo: "))
            ancho = int(input("Ancho del rectangulo: "))

            area = largo*ancho

            return area
    except Exception as e:
        return e



if __name__ == "__main__":
    figura:str = input("Escriba el poligono a calcular (triangulo, cuadrado, rectangulo): ").lower()
    area = poligono(figura)

    print(f"El area del {figura} es: {area}")
