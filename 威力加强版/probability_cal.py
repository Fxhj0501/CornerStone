import stop_init
import fee_cal
from math import *

'''
ALPHA为全局变量，表示信息素的重要程度，反映了蚂蚁在运动过程中积累的信息量在蚁群搜索中的重要性
BETA也为全局变量，代表启发式因子，其大小反映了蚁群遍历过程中确定性因素的作用强度
'''


def pb_cal(ALPHA, BETA):  # 计算各点到各点的概率
