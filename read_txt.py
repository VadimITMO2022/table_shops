import numpy as np

def extract_from_file():

    with open("data\\file.txt", "r") as file:
        k=0
        data=[]
        for line in file:
            k+=1
            my_list=[]
            split_line = line.split()
          #  my_list.append(int(split_line[0]))
          #  my_list.append(int(split_line[1]))
          #  my_list.append(int(split_line[2]))
          #  my_list.append(float(split_line[3]))

            my_list.append(split_line[0])
            my_list.append(split_line[1])
            my_list.append(split_line[2])
            my_list.append(split_line[3])
            data.append(my_list)
        data.pop(0) # удаляем 0-й элемент из списка data (с названиями колонок)

    return data
            

