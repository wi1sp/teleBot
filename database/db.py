#create database in python with mysql
#pip3 install mysql-connector-python
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

def get_days():
    select_query = f"""
            select d.Id, d.Name from days d;
        """
    try:
        with connect(
                host="localhost",
                user="root",
                password="root",
                database="university_info"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                result = cursor.fetchall()
                mas = []
                for row in result:
                    mas.append(row)
                return mas
    except Error as e:
        print(e)

def get_timetable(day_Id):
    select_query = f"""
        select d.Name, t.Subject_Num ,s.Name, st.Name from timetable t
        join days d on d.Id = t.Day_Id
        join subject_type st on st.Id = t.Type_Id
        join subjects s on s.Id = t.Subject_Id
        where t.Day_Id = {day_Id}
        order by t.Day_Id, t.Subject_Num
    """
    try:
        with connect(
                host="localhost",
                user="root",
                password="root",
                database="university_info"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                result = cursor.fetchall()
                mas = []
                for row in result:
                    mas.append(row)
                return mas
    except Error as e:
        print(e)