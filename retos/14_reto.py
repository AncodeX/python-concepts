# validar una dominio https://www.google.com
import re, requests

content = requests.get("http://www.gutenberg.org/files/1112/1112.txt").text

dominio = re.findall(r"https?://[\w\.-]+\.[a-zA-Z]{2,}", content)

correo = "12papas-_to@caspepemalo"
pattern = r"^[\w\d\.-]+@[\w\.-]+\.\w+$"

correo_validado = re.match(pattern, correo)

