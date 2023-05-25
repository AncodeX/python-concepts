from string import ascii_letters, digits, hexdigits
from random import choices, randint, shuffle
from sys import argv


def random_user_id():
    char = ascii_letters + digits

    for i in range(int(argv[2])):
        password = "".join(choices(char, k=int(argv[1])))
        print(i+1, password)

def rgb_color_gen():
    x = [str(randint(0, 255)) for i in range(3)]
    rgb = f"rgb({','.join(x)})"

    return rgb

def  hexa_colors():
    x = choices(hexdigits, k=6)   

    hex = "#" + "".join(x)

    return hex


def generate_colors(t:str, n:int):
    rgb = rgb_color_gen()
    hex = hexa_colors()

    if t != "":
        x = [rgb if t == "rgb" else hex if t == "hexa" else "" for i in range(n)]

        print(x)

def  shuffle_list(x:list):
    shuffle(x)

    print(x)

if __name__ == "__main__":
    animal = ["Bird", "Hourse", "Dog", "Cat", "Cow", "Fox", "Wolf"]
    shuffle_list(animal)