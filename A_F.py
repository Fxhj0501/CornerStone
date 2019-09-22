import random
import numpy as np
import matplotlib.pyplot as plt
from math import *


class Map:
    def __init__(self):  # 50个地点的初始化
        self.location = np.random.random(100) * 100  # 产生100个随机数
        self.location_x = []
        self.location_y = []
        self.stop = np.random.rand(100) * 10  # 产生停滞系数与停滞时间
        self.stop.self.stop.reshape(50, 2)  # 区分先后
        self.dev = np.random.rand(50, 1) * 10  # 确定发达系数
        self.fee = 1  # 单位发达系数路费
        self.pheromone = np.ones((50, 50))  # 初始化信息素矩阵，全为1，要产生为一个对称矩阵
        for i in range(0, 50):
            self.pheromone[i][i] = 0  # 清空对角，自己对自己的信息浓度为0

    def set_xy(self):
        for i in range(0, 100):  # 为了后期作图方便，获得坐标的X值和Y值
            if i % 2 == 0:
                self.location_x.append(self.location[i])
            elif i % 2 == 1:
                self.location_y.append(self.location[i])
        self.location = self.location.reshape(50, 2)

    def get_x(self):
        return self.location_x

    def get_y(self):
        return self.location_y


class Antish:
    def __init__(self):
        self.num = 100  # 蚂鱼的数量
        self.ph = 70  # 按照信息素走的蚂鱼数
        self.ran = 30  # 随机走的鱼蚁数量，防止陷入局部最优解，取自鱼群
        self.pheromone_max = 8  # 拥挤度因子，防止陷入局部最优解，取自鱼群


alpha = 1  # 信息素重要程度，反映了蚂蚁在运动过程中积累的信息量在蚁群搜索中的重要性
beta = 5  # 启发函数因子，反映了启发式信息在知道蚁群搜索过程中的相对重要程度，其大小反映了蚁群遍历过程中确定性因素的作用强度
iter_times = 0  # 初始化迭代次数
iter_max = 1000  # 最大迭代次数
rho = 0.2  # 信息素挥发因子
real_map = Map()  # 创建地图对象
real_map.set_xy()  # 初始化地图
fellows = Antish()  # 创建蚂鱼
fee_matrix = np.zeros(50, 50)
stop_cost = []


def fee_cal():  # 得到路线费用矩阵
    for i in range(0, 50):
        for j in range(0, 50):
            if i == j:
                pass
            if i != j:
                coo = real_map.location
                dis = sqrt(pow(coo[i][0] - coo[j][0], 2) + pow(coo[i][1] - coo[j][1], 2))  # 欧氏距离
                fee = dis * real_map.fee * (real_map.dev[i] * real_map.dev[j])  # 费用计算
                fee_matrix[i][j] = fee
                fee_matrix[j][i] = fee  # 得到两点间的对称矩阵
    return fee_matrix


fee_matrix = fee_cal()  # 更新费用矩阵,得到一个50*50的对称矩阵


def stop_cal_expectation():  # 停滞量计算，用于确定蚂鱼到对应城市的期望值，来得到启发式函数
    for i in range(0, 50):
        temp = pow(real_map.stop[i][0], real_map.stop[i][1])  # 第一列是系数，第二列是时间
        stop_cost.append(1 / temp)
    return stop_cost


stop_cost = stop_cal_expectation()  # 初始化停滞量函数，得到一个1*50的矩阵


def probability(i, j):  # 利用轮盘赌来计算蚂鱼走向哪个节点，这个函数用来计算两地点之间的概率
    # i为当前所在地点，j为要去的城市
    p_sum = 0
    for k in range(0, len(permission)):  # 对于该蚂鱼当前所有可以走的地点
        location_index = permission[k]  # 获取可去城市的编号
        # 计算可行路径的概率
        p_sum += pow(real_map.pheromone[i][location_index], alpha) * pow(((1 / fee_matrix[i][location_index]) *
                                                                          stop_cost[location_index]), beta)
    p_now = pow(real_map.pheromone[i][j], alpha) * pow((1 / fee_matrix[i][j]) * stop_cost[j], beta)  # 计算转移到j的概率
    p = p_now / p_sum
    return p


def gamble(i):  # 轮盘赌函数，传入当前城市
    p_location_list = []
    p_sum = 0
    for k in range(0, len(permission)):
        location_index = permission[k]  # 同上，获取地点编号
        p_current = probability(i, location_index)
        p_location_list.append(p_current)  # 将其加入同一个list，它存了i到所有地点的概率
        # 且这样地点的下标和概率的下标是一一对应的
        p_sum += p_current
    p_location_list.sort()
    p_choose = random.uniform(0, p_sum)
    chosen_index = 0
    for m in range(0, len(p_location_list)):  # 自制简陋轮盘赌，概率带为左开右闭
        if m == 0:
            if p_choose <= p_location_list[m]:
                chosen_index = m
            else:
                pass
        else:
            if p_choose < p_location_list[m]:
                chosen_index = m
    return permission[chosen_index]  # 返回地点编号


while iter_times <= iter_max:
    permission = np.linspace(0, 49, num=50, endpoint=True, retstep=False)  # 初始化最初能去的城市
    taboo = []  # 初始化不能去的城市
    for i in range(0, fellows.ph):  # 按照信息素浓度走的蚂鱼


