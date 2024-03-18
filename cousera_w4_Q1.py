cost_single = int(input())
price = int(input())
count = int(input())
order = int(input())
cost_tol = cost_single * order

earn = 0.0
pos_tol = 0.0
for i in range(count+1):
    pos = float(input())
    if i < order:
        earn += i * price * pos
    elif i == order:
        earn += i * price * (1-pos_tol)
    pos_tol += pos

print(f'{int(earn - cost_tol)}')
