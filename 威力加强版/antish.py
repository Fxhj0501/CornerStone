class Antish:
    def __init__(self):
        self.num = 100  # 蚂鱼的数量
        self.ph = 70  # 按照信息素走的蚂鱼数
        self.ran = 30  # 随机走的鱼蚁数量，防止陷入局部最优解，取自鱼群
        self.pheromone_max = 8  # 拥挤度因子，防止陷入局部最优解，取自鱼群