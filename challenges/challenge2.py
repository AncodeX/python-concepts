from random import choice, randint
from string import ascii_letters, digits, punctuation, hexdigits
import sys

# Ejercico 1

def random_user_id():
    try:
        characters = ascii_letters + digits + punctuation
        for i in range(int(sys.argv[2])):
            print("".join(choice(characters) for i in range(int(sys.argv[1]))))
    except Exception as e:
        print(f"Error: {e}")

# Ejercicio 2

def rgb_color_gen():
    n = [randint(0, 255) for i in range(3)]
    return f"rgb({n[0]},{n[1]},{n[2]})"

def list_of_hexa_colors():
    return "#" + "".join(choice(hexdigits) for i in range(6))

def generate_colors(type, n):
    if type.lower() == "rgb":
        return [rgb_color_gen() for i in range(n)]
    elif type.lower() == "hexa":
        return [list_of_hexa_colors() for i in range(n)]

# Ejercicio 3

def shuffle_list(array):
    return [choice(array) for i in range(len(array))]

def random_array():
    return [randint(0, 9) for i in range(7)]

if __name__ == "__main__":
    pass