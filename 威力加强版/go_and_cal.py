import stop_init
import fee_cal
from math import pow
import ph_map_init
import random
import antish
import sys
sys.setrecursionlimit(100000000)

'''
ALPHA为全局变量，表示信息素的重要程度，反映了蚂蚁在运动过程中积累的信息量在蚁群搜索中的重要性
BETA也为全局变量，代表启发式因子，其大小反映了蚁群遍历过程中确定性因素的作用强度
'''

PH = ph_map_init.Pheromone_Map()
ANTISH = antish.Antish()


def rand_go():  # 蚂鱼随机走的程序
    while len(ANTISH.taboo) < 10:
        temp = random.randint(0, 9)
        if temp not in ANTISH.taboo:
            ANTISH.taboo.append(temp)
    routine = ANTISH.taboo
    ANTISH.reset_taboo()
    return routine


class Go_Cal:
    def __init__(self, ALPHA, BETA, RHO):  # 构造器中把参传进来
        self.alpha = ALPHA
        self.beta = BETA
        self.rho = RHO
        self.ph_map = PH.get_map()
        self.fee_matrix = fee_cal.get_fee()
        self.stop = stop_init.stop_cal()
        self.ph_max = ANTISH.pheromone_max

    def all_path(self, i):  # 计算当前蚂鱼所在点到所有点的概率, 在next_go中调用
        path_pb = []
        for k in range(0, 10):
            if k != i and k not in ANTISH.taboo:  # 这里排除了已经去过的点
                tau = pow(self.ph_map[i][k], self.alpha)  # 考虑信息素浓度
                artificial = 1 / (self.fee_matrix[i][k] * self.stop[k])
                eta = pow(artificial, self.beta)  # 启发式因子，考虑纯外界因素
                path_pb.append(tau * eta)  # 得到 i 到 各点的倾向
            else:
                path_pb.append(0)  # 如果到自己或去禁忌表中的地方，倾向为0
        pb_sum = sum(path_pb)
        for k in range(0, 10):  # 把可能性转化为概率
            path_pb[k] = round(path_pb[k] / pb_sum, 4)  # 保留小数点后四位
        return path_pb

    def next_go(self, i):  # i是当前蚂鱼所在的点
        pb = self.all_path(i)
        cur_pb = random.random()
        next_station = None
        for k in range(0, 10):
            if pb[k] >= cur_pb:
                if k not in ANTISH.taboo:  # 不在禁忌表中才可以去
                    next_station = k
                else:
                    pass
        if next_station is None:  # 如果没找出来，继续找
            next_station = self.next_go(i)
        return next_station

    def ph_go(self):  # 确定按照信息素浓度走的每一只蚂鱼的路线，计算成本
        start = random.randint(0, 9)  # 随机选一个起点
        ANTISH.taboo.append(start)
        temp = start
        while len(ANTISH.taboo) < 10:  # 还有点可以去的时候
            temp = self.next_go(temp)  # 下一个要去的点
            ANTISH.taboo.append(temp)  # 将下一个要去的点加入禁忌表
        routine = ANTISH.taboo
        ANTISH.reset_taboo()  # 清空禁忌表
        return routine

    def update(self, routine):  # 更新信息素
        self.ph_map *= (1 - self.rho)  # 挥发信息素
        for t in range(0, 9):  # 走过的路上增添信息素
            cost = self.fee_matrix[routine[t]][routine[t+1]]
            self.ph_map[routine[t]][routine[t+1]] += (1 / cost)
            self.ph_map[routine[t + 1]][routine[t]] += (1 / cost)
            if self.ph_map[routine[t]][routine[t + 1]] > self.ph_max:  # 限制信息素
                self.ph_map[routine[t]][routine[t + 1]] = self.ph_max
                self.ph_map[routine[t + 1]][routine[t]] = self.ph_max
            else:
                pass


if __name__ == "__main__":
    test = Go_Cal(3, 2, 0.05)
    # print(test.fee_matrix)
    # print(test.stop)
    # print(test.ph_map)
    for i in range(0, 30000):
        print(test.ph_go())


