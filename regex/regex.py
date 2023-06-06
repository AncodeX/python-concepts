import re, requests

response = requests.get("http://www.gutenberg.org/files/1112/1112.txt")
txt = response.text

#\d -> Busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d", txt)

# \D -> Busca TODO menos digitos numericos del 0 - 9
#resultado = re.findall(r"\D", txt)

# \w -> Busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w", txt)

# \W -> Busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W", txt)

# \s -> Busca espacios en blanco, tabs, saltos de linea
#resultado = re.findall(r"\s", txt)

# \S -> Busca TODO MENOS espacios en blanco, tabs, saltos de linea
#resultado = re.findall(r"\S", txt)

# \n -> Busca saltos en linea
#resultado = re.findall(r"\n", txt)

# . Busca TODO MENOS saltos en linea
#resultado = re.findall(r".", txt)

# \ -> cancelar caracteres especiales
#resutlado = re.findall(r"\.", txt)

# ^ -> busca el comienzo de una linea
#resultado = re.findall(r"Hola", txt, re.M)

# $ -> Busca el final de una linea
#resultado = re.findall(r"Hola$", txt)

# {n,m} -> Rango n veces
resultado = re.findall(r"\d{1,4}", txt)

print(resultado)