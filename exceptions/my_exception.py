class MyException(Exception):
    def __init__(self, err):
        print(f"ERROR: '{err}'")
    

def main(x:int, y:str):
    try:
        print(x + y)

    except TypeError:
        print(TypeError("jajaja"))


main(2, "e")