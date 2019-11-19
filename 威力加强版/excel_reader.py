import xlrd


def read():
    # load the excel file
    book = xlrd.open_workbook("MapInformation.xls")

    # which sheet
    sheet = book.sheet_by_index(0)

    # get the location
    x = sheet.col_values(0)  # 获取 x坐标
    y = sheet.col_values(1)  # 获取 y坐标
    stop_para = sheet.col_values(2)  # 获取 停滞系数
    stop_time = sheet.col_values(3)  # 获取 停滞时间
    dev_para = sheet.col_values(4)  # 获取 发达系数
    # 以下几步去掉表头
    x = x[1:]
    y = y[1:]
    stop_para = stop_para[1:]
    stop_time = stop_time[1:]
    dev_para = dev_para[1:]
    return x, y, stop_para, stop_time, dev_para


X, Y, Stop_Para, Stop_Time, Dev_Para = read()


def read_x():
    return X


def read_y():
    return Y


def read_sp():
    return Stop_Para


def read_st():
    return Stop_Time


def read_dp():
    return Dev_Para


if __name__ == "__main__":
    pass
