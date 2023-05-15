# Modulo del sistema operativo. Realiza muchas tareas automaticas del sistema
import os

""" 
Obtener argumentos cuando se ejecuta un script:
    python module.py arg1 arg2 ...
"""

import sys

"""
Obtengo el nombre de usuario del sistema
"""
from getpass import getuser

import statistics

def main():
    dir_name = input("Nombre del directorio: ")
    if sys.argv[1] == "add":
        os.mkdir(dir_name)
    elif sys.argv[1] == "remove":
        os.rmdir(dir_name)
    elif sys.argv[1] == "get":
        cwd = os.getcwd()
        print(cwd)
    elif sys.argv[1] == "change":
        os.chdir("./modules")

if __name__ == "__main__":
    main()

# Function to Get the current  
# working directory 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
    
    
# Driver's code 
# Printing CWD before 
current_path() 
    
# Changing the CWD 
os.chdir(f'C:\\Users\\{getuser()}') 
    
# Printing CWD after 
current_path()

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(statistics.mean(ages))       # ~22.9
print(statistics.median(ages))     # 22
print(statistics.mode(ages))       # 20
print(statistics.stdev(ages))      # ~6.1

