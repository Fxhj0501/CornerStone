import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib as mpl

def run():
    # data = pd.read_excel("画图顺序.xlsx", header=None)
    x = [65, 39, 85, 8, 69, 31, 40, 22, 79, 31]
    y = [71, 10, 3, 76, 65, 89, 60, 48, 20, 95]
    r = [3, 1, 4, 1, 7, 10, 9, 2, 10, 1]
    c = [1.3125, 3.0729, 1.0001, 4.4096, 3.0729, 29.2144, 4.0081, 5.0027, 15.5536, 9.0009]
    c = list(map(lambda a: a + a * 100 % 100, c))
    # x = list(data[1][2:12])
    # y = list(data[2][2:12])
    # r = list(data[3][2:12])
    # c = list(data[4][2:12])
    area = np.pi * 5 * np.array(r) ** 2
    plt.ion()  # 开启interactive mode 成功的关键函数
    plt.figure(1)
    order_us = [1, 2, 8, 4, 0, 6, 7, 3, 5, 9]
    order_traditional = [3, 6, 0, 4, 2, 8, 1, 7, 5, 9]
    order_greedy = [3, 5, 9, 6, 4, 0, 8, 2, 1, 7]
    us_save_num1 = []
    us_save_num2 = []
    tra_save1 = []
    tra_save2 = []
    greedy_save1 = []
    greedy_save2 = []
    for i in range(0, 10):
        plt.clf()  # 清空画布上的所有内容
        # us
        plt.subplot(1, 3, 1)
        plt.scatter(x, y, s=area, c=c)
        plt.title("Mixed Algorithm")
        us_save_num1.append(x[order_us[i]])
        us_save_num2.append(y[order_us[i]])
        plt.plot(us_save_num1, us_save_num2, 'r')
        # traditional
        plt.subplot(1, 3, 2)
        plt.scatter(x, y, s=area, c=c)
        plt.title("Traditional Ant Colony Algorithm")
        tra_save1.append(x[order_traditional[i]])
        tra_save2.append(y[order_traditional[i]])
        plt.plot(tra_save1, tra_save2, 'b')
        # force
        plt.subplot(1, 3, 3)
        plt.scatter(x, y, s=area, c=c)
        plt.title("Greedy Algorithm")
        greedy_save1.append(x[order_greedy[i]])
        greedy_save2.append(y[order_greedy[i]])
        plt.plot(greedy_save1, greedy_save2, 'g')
        plt.colorbar()

        plt.pause(0.5)

    plt.pause(600)
