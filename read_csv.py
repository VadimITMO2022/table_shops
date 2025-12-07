import numpy as np
import csv

def extract_from_csv_file():
    FILENAME = "data\\file.csv"   
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        data=[]
        for row in reader:
           my_list=[]
           my_list.append(row[0])
           my_list.append(row[1])
           my_list.append(row[2])
           my_list.append(row[3])

        #   my_list.append(int(float(row[0])))
        #   my_list.append(int(float(row[1])))
        #   my_list.append(int(float(row[2])))
        #   my_list.append(float(row[3]))
           data.append(my_list)

        data.pop(0) # удаляем 0-й элемент из списка data (с названиями колонок)

    return data
