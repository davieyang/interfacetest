# -*- coding: utf-8 -*-
# @Time    : 10/30/2019 7:05 PM
# @Author  : davieyang
# @Email   : davieyang@qq.com
# @File    : util_mysql.py
# @Project: Interface_Python_T
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cpparser


base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

config_file_path = u'D:\\PythonPrograms\\Interface_Python_T\\configuration\\db_config.ini'
cf = cpparser.ConfigParser()
cf.read(config_file_path, 'utf-8')
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


class Data_Base_Handler:

    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor

            )
        except OperationalError as e:
            # raise e
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def delete_data_from_table(self, table_name):
        sql_string_for_delete = "delete from" + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECK=0;")
            cursor.execute(sql_string_for_delete)
        self.conn.commit()

    def insert_data_into_table(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        sql_string_for_insert = "INSERT INTO" + table_name + "(" + key + ") VALUES (" + value + ")"
        print(sql_string_for_insert)
        with self.conn.cursor() as cursor:
            cursor.execute(sql_string_for_insert)
        self.conn.commit()

    def close_database_connection(self):
        self.conn.close()


if __name__ == '__main__':
    db = Data_Base_Handler()
    table_name = "sign_event"
    table_data = {'id': 12, 'name': 'davieyang', 'limit': 20000, 'status': 1,
                  'address': 'guangzhou', 'start_time': '2019-10-31 00:00:00'}
    db.delete_data_from_table(table_name)
    db.insert_data_into_table(table_name, table_data)
    db.close_database_connection()
