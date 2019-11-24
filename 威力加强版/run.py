import go_and_cal
import antish


testers = antish.Antish()
runner = go_and_cal.Go_Cal(2, 3, 0.05)  # alpha beta rho
iter_times = 0  # 初始化迭代次数
iter_max = 300  # 最大迭代次数
for i in range(0, int(iter_max)):
    for j in range(0, testers.ran):  # 先随机蚂鱼走
        runner.update(go_and_cal.rand_go())
    for j in range(0, testers.ph):  # 所有按照信息素走的蚂鱼
        runner.update(runner.ph_go())
print(runner.ph_map)


def cost_cal(routine):
    cost = 0
    for k in range(0, 9):
        cost += runner.fee_matrix[routine[k]][routine[k+1]]
    return cost


print(runner.ph_go())
print(cost_cal(runner.ph_go()))