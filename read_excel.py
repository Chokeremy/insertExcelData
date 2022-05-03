import pandas as pd

class ReadXlsx:
    """读写表格"""

    def __init__(self, excel_path):

        # 设置显示最大行数：max_rows，最大列数：max_columns
        pd.options.display.max_rows = 1000
        # 读取excel文件，usecols='G, S'指定G，S列，usecols=[1, 2]指定1，3列
        self.result_action = pd.read_excel(io=excel_path, usecols='G, S')

    def read_data(self):

        result = []
        # 读取的数据转化成二元列表进行遍历
        for i in self.result_action.values.tolist():
            result.append(i)

        return result


print(ReadXlsx(r'data\CDSS_BASE_V1.0.0_20220429.xlsx').read_data())
