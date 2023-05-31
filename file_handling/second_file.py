with open(file="file_handling/file.txt", mode="a+", encoding="UTF-8") as txt:
    txt.writelines(['Colombia es un pais biodiverso y multicultural lleno de riqueza\n', 'Que onda tan chevere solo nos falta cero corrupcion\n', 'No siga leyendo\n', '\n', 'No se me ocurre mas por escribir\n', 'Falta de creatividad'])
    lines = txt.read().splitlines()
    print(lines)

    