# -*- coding:utf-8 -*-
import xlrd
import pandas as pd

def xlsx_to_csv():
    data_xls = pd.read_excel('F:\\AnacondaPython3_6\\PycharmWork\\xlxs_To_csv\\attackData.xlsx', index_col=0)
    data_xls.to_csv('F:\\AnacondaPython3_6\\PycharmWork\\xlxs_To_csv\\attackData.csv', encoding='utf-8')

if __name__ == '__main__':
    xlsx_to_csv()