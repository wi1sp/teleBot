#pip3 install mysql-connector-python

import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

def get_days():
    select_query = f"""
            select d.Id, d.Name from days d;
        """
    return execute_query(select_query)

def get_timetable(day_Id):
    select_query = f"""
        select d.Name, t.Subject_Num ,s.Name, st.Name from timetable t
        join days d on d.Id = t.Day_Id
        join subject_type st on st.Id = t.Type_Id
        join subjects s on s.Id = t.Subject_Id
        where t.Day_Id = {day_Id}
        order by t.Day_Id, t.Subject_Num
    """
    return execute_query(select_query)

def get_dz(day_Id):
    select_query = f"""
            select s.Name, dz.Description from dz
            join days d on d.Id = dz.Day_Id
            join subjects s on s.Id = dz.Subject_Id
            where Day_Id = {day_Id} order by Subject_Id
        """
    return execute_query(select_query)

def get_materials():
    select_query = f"""
                select s.Name, m.Ref from materials m
                join subjects s on s.Id = m.Subject_Id;
            """
    return execute_query(select_query)
def get_contacts():
    select_query = f"""
                select pr.Fio, c.Post_Id, p.Name, c.Ref from contacts c
                join persons pr on pr.Id = c.Person_Id
                join posts p on p.Id = c.Post_Id;
            """
    return execute_query(select_query)

def execute_query(select_query):
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