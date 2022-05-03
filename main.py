import imp
from tkinter import E
from database import PgsqlConnect
from read_file import ReadFile
from read_excel import ReadXlsx
from config import *


class InsertFileData:
    """插入文件数据"""

    @staticmethod
    def insert_file_data():

        # 实例化ReadFile读写文件类调用读写文件方法返回二元列表数据
        file_data_list = ReadFile(FILE).open_file()
        # 实例化PgsqlConnect数据库操作类
        obj = PgsqlConnect(DATABASE_NAME, USER, PASSWORD, HOST, PORT)
        # 统计插入多少个
        n = 0
        for data in file_data_list:
            try:
                sql = "update medical_knowledge.action set alert_msg = '{}' where id = '{}'".format(data[1], data[0])
                obj.pgsql_execute(sql)
                n += 1
                print('\rUpdate语句执行进度：{}%\tUpdate语句执行条数：{}'.format(round((file_data_list.index(data) + 1) /
                                                                         len(file_data_list) * 100, 2), n), end='')
            except Exception as e:
                print('异常信息：{}'.format(e))


class InsertExcelData:
    """插入excel数据"""

    @staticmethod
    def insert_excel_data():

        # 实例化ReadXlsx读写表格类调用读写表格方法返回二元列表数据
        excel_data_list = ReadXlsx(EXCEL).read_data()
        # 实例化PgsqlConnect数据库操作类
        obj = PgsqlConnect(DATABASE_NAME, USER, PASSWORD, HOST, PORT)

        n = 0

        for data in excel_data_list:
            try:
                sql = "update medical_knowledge.action set alert_msg = '{}' where id = '{}'".format(data[1], data[0])
                obj.pgsql_execute(sql)
                n += 1
                print('\rUpdate语句执行进度：{}%\tUpdate语句执行条数：{}'.format(round((excel_data_list.index(data) + 1) /
                                                                         len(excel_data_list) * 100, 2), n), end='')
            except Exception as e:
                print('异常消息：{}'.format(e))


if __name__ == '__main__':

    # InsertFileData().insert_file_data()

    InsertExcelData().insert_excel_data()

