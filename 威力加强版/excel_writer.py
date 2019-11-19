import numpy as np
import math
import xlrd
import xlwt
from xlutils.copy import copy


# x = list(map(int, np.random.random(50) * 100))
# y = list(map(int, np.random.random(50) * 100))
# stop_para = list(map(math.ceil, np.random.random(50) * 10))
# stop_time = list(map(math.ceil, np.random.random(50) * 10))
# dev_para = list(map(math.ceil, np.random.random(50) * 10))
local_path = r"MapInformation.xls"


def write_excel_xls_append(path, value, which_col):
    index = len(value)  # how many rows to write
    workbook = xlrd.open_workbook(path)  # open the workbook
    sheets = workbook.sheet_names()  # obtain the whole sheets
    worksheet = workbook.sheet_by_name(sheets[0])  # the first sheet
    # rows_old = worksheet.nrows  # how many exited rows
    new_workbook = copy(workbook)  # xlrd convert to xlwt
    new_worksheet = new_workbook.get_sheet(0)  # obtain the converted first sheet
    for i in range(0, index):
        new_worksheet.write(i+1, which_col, value[i])  # write the data, here beginning from row = 1
    new_workbook.save(path)  # save
    print("Success!")


