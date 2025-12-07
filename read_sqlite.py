import sqlite3;
import sys
 
def extract_from_sqlite(sql_name): 
 #   con = sqlite3.connect("data\\shops.db")  # соединяемся с БД
    con = sqlite3.connect(sql_name)  # соединяемся с БД
    cursor = con.cursor()    # создаем курсор
    cursor.execute("SELECT * FROM goods")  # извлекаем данные из таблицы goods

    data = []   # создаем пустой список строк таблицы
    
    for good in cursor.fetchall(): 
        my_list=[]  # создаем пустой список элементов одной строки в таблице
        for g in good:
            my_list.append(g) # добавляем все элементы строки в список my_list
        data.append(my_list) # добавляем все строки в список data


    return data




    
      

    
