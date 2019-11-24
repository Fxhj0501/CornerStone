class Antish:
    def __init__(self):
        self.num = 100  # 蚂鱼的数量
        self.ph = 90  # 按照信息素走的蚂鱼数
        self.ran = 10  # 随机走的鱼蚁数量，防止陷入局部最优解，取自鱼群
        self.pheromone_max = 2  # 拥挤度因子，防止陷入局部最优解，取自鱼群
        self.taboo = []

    def reset_taboo(self):  # 重置禁忌表
        self.taboo = []

