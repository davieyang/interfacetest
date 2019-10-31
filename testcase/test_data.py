# -*- coding: utf-8 -*-
# @Time    : 10/31/2019 11:42 AM
# @Author  : davieyang
# @Email   : davieyang@qq.com
# @File    : test_data.py
# @Project: Interface_Python_T
import sys
sys.path.append('configuration')
from utl.util_mysql import Data_Base_Handler

datas = {
    'sign_event': [
        {},
        {},
        {},
        {},
        {}
    ],
    'sign_guest': [
        {},
        {},
        {},
        {},
        {}
    ]
}


def init_data():
    db=Data_Base_Handler()
    for table, data in datas.items():
        db.delete_data_from_table(table)
        for d in data:
            db.insert_data_into_table(table, d)
        db.close_database_connection()


if __name__ == '__main__':
    init_data()