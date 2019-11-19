import excel_reader
from math import *


def stop_cal():  # 计算停滞损耗，来得到启发式函数，用于代入鱼蚁走到该城市的期望值
    # 停止损耗 = 停滞系数 ^ 停滞时间
    stop_cost = []
    stop_para = excel_reader.read_sp()
    stop_time = excel_reader.read_st()
    for i in range(0, len(stop_para)):
        temp = pow(stop_para[i], stop_time[i])
        stop_cost.append(temp % 13)
    return stop_cost


if __name__ == "__main__":
    test = stop_cal()
    print(test)