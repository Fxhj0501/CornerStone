import go_and_cal
import antish


testers = antish.Antish()
runner = go_and_cal.Go_Cal(2, 3, 0.05)  # alpha beta rho
iter_max = 300  # 最大迭代次数
for i in range(0, int(iter_max)):
    for j in range(0, 100):  # 全是随机蚂鱼走
        runner.update(go_and_cal.rand_go())


def cost_cal(routine):
    cost = 0
    for k in range(0, 9):
        cost += runner.fee_matrix[routine[k]][routine[k+1]]
    return cost


print(go_and_cal.rand_go())
print(cost_cal(go_and_cal.rand_go()))
