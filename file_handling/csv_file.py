import csv

with open("file_handling/file.csv", encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=",")
    delimitador = 0
    for row in csv_file:
        print(row)