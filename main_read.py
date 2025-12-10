import numpy as np
import sys
#from read_postgresql import extract_from_postgresql
from read_sqlite import extract_from_sqlite
from read_sqlalchemy import extract_from_sqlalchemy
#from console_id import print_to_console_id
#from write_console2 import print_to_console
from read_txt import extract_from_file
from read_csv import extract_from_csv_file
#from dotenv import load_dotenv
import os #библиотека операционной системы


def calculate_data(k):
    if k==1 or k==2:
       sql_name="shops.db"

    '''
    if k==3 or k==4:
        load_dotenv()  #загрузить секретные ключи

        f_dbname = os.getenv("f_dbname")
        f_host = os.getenv("f_host")
        f_user = os.getenv("f_user")
        f_password = os.getenv("f_password")
        f_port = os.getenv("f_port")
    '''

    if k ==1:
        data=extract_from_sqlite(sql_name) # извлечь из БД SQLite
    elif k ==2:
        sql_database = "sqlite:///"+sql_name
        data=extract_from_sqlalchemy(sql_database) # извлечь из БД  SQLAlchemy            
  #  elif k ==3:
  #      data=extract_from_postgresql(f_dbname,f_host,f_user,f_password,f_port) # извлечь из БД PostgreSQL
  #  elif k ==4:
  #      sql_database = "postgresql://"+f_user+":"+f_password+"@"+f_host+":"+f_port+"/"+f_dbname
  #      data=extract_from_sqlalchemy(sql_database) # извлечь из БД  SQLAlchemy       
    elif k==5:
        data=extract_from_file() # извлечь из текстового файла
    elif k==6:
        data=extract_from_csv_file() # извлечь из файла csv
    return data

# k=6
# data = calculate_data(k)
# print_to_console(data,k) # напечатать в консоль


