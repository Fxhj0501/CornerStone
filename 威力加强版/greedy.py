import fee_cal
fee_matrix = fee_cal.get_fee()
path = []
cost = 0
available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start = 9
available.remove(start)
current = start
path.append(start)
while available:
    current_cost_list = []
    for station in available:
        current_cost_list.append(fee_matrix[current][station])
    min_cost = min(current_cost_list)
    cost += min_cost
    for station in available:
        if fee_matrix[current][station] == min_cost:
            current = station
            available.remove(current)
            path.append(current)
print(path)
print(cost)