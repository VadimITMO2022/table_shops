from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String, Float
import sys

def extract_from_sqlalchemy(sql_database): 
   # sqlite_database = "sqlite:///data\\shops_alchemy.db"
    engine = create_engine(sql_database, echo=False)
    
    class Base(DeclarativeBase): pass
    # создаем модель, объекты которой будут храниться в бд
    class Good(Base):
        __tablename__ = "goods"
        id = Column(Integer, primary_key=True, index=True)
        id_shop = Column(Integer)
        id_good = Column(Integer)
        amount = Column(Integer)
        price = Column(Float)
    
    Base.metadata.create_all(bind=engine)
    
    with Session(autoflush=False, bind=engine) as db:
        # получение всех объектов
        people = db.query(Good).all()
        data = []   # создаем пустой список строк таблицы

        for p in people: 
            my_list=[]  # создаем пустой список элементов одной строки в таблице
            my_list.append(p.id) # добавляем все элементы строки в список my_list
            my_list.append(p.id_shop)
            my_list.append(p.id_good)
            my_list.append(p.amount)
            my_list.append(p.price)
            data.append(my_list) # добавляем все строки в список data

    return data

       
  