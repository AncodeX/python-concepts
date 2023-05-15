def main(x:int, y:int):
    try:
        print(x + y)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(2, "2")