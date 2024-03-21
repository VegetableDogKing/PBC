cost_single = int(input())
price = int(input())
count = int(input())
left = int(input())
pos_list = []
for i in range(count+1):
    pos_list.append(float(input()))

earn_best = 0
order_best = 0
for order in range(count+1):
    cost_tol = cost_single * order
    earn = 0.0
    pos_tol = 0.0
    for i in range(order+1):
        pos = pos_list[i]
        if i < order:
            earn += (i * price + left * (order - i)) * pos
        elif i == order:
            earn += i * price * (1-pos_tol)
        pos_tol += pos
        
    earn = earn - cost_tol
    if earn > earn_best:
        earn_best = earn
        order_best = order

print(f'{order_best} {int(earn_best)}')
