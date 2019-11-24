import numpy as np


class Pheromone_Map:
    def __init__(self):
        self.ph_map = np.ones((10, 10))  # 初始化信息素浓度，最初每条路的信息素为1
        for i in range(0, 10):
            self.ph_map[i][i] = 0  # 自己对自己的信息素浓度为0，清空对角线

    def get_map(self):
        return self.ph_map


if __name__ == "__main__":
    test = Pheromone_Map()
    print(test.ph_map)