import numpy as np
import excel_reader
from math import *


class Fee_Matrix:
    def __init__(self):
        # 获得坐标信息及各点发达系数
        self.x = excel_reader.read_x()
        self.y = excel_reader.read_y()
        self.dev_para = excel_reader.read_dp()
        self.fee = np.zeros((10, 10))  # 初始化一个全是零的费用矩阵
        self.unit_fee = 1  # 每一单位距离所画的费用

    def fee_cal(self):  # 计算路线费用矩阵
        for i in range(0, 10):
            for j in range(0, 10):
                if i != j:
                    # 计算任意两点欧氏距离，并形成对称矩阵
                    dis = sqrt(pow(self.x[i] - self.x[j], 2) + pow(self.y[i] - self.y[j], 2))
                    # 发达系数的用法： 综合发达系数： 2 / （i的发达系数 + j的发达系数）
                    current_fee = dis * self.unit_fee * (2 / (self.dev_para[i] + self.dev_para[j]))
                    self.fee[i][j] = round(current_fee, 2)  # 保留两位小数
                    self.fee[j][i] = round(current_fee, 2)
                    #  对称矩阵，对角线都为0


temp = Fee_Matrix()
temp.fee_cal()
fee_matrix = temp.fee


def get_fee():
    return fee_matrix


if __name__ == "__main__":
    a = get_fee()
    print(a)
