tasks_count = int(input())
order_count = tasks_count + 1

process_time = input().split(',')
deadline = input().split(',')
order_origin = input().split(',')

for i in range(tasks_count):
    process_time[i] = int(process_time[i])
    deadline[i] = int(deadline[i])
    order_origin[i] = int(order_origin[i])

index = 0
order = []
order.append(order_origin)
while True:
    order_origin = order[index].copy()
    order = []
    order.append(order_origin.copy())
    for i in range(tasks_count):
        order.append(order_origin.copy())
        tmp = order[i+1][i]
        order[i+1][i] = order[i+1][(i+1) % tasks_count]
        order[i+1][(i+1) % tasks_count] = tmp

    delay_tol = [0] * order_count
    time = [0] * order_count
    for i in range(tasks_count):
        for j in range(order_count):
            time[j] += process_time[order[j][i]-1]
            delay = time[j] - deadline[order[j][i]-1]
            if delay > 0:
                delay_tol[j] += delay

    index = 0
    delay_min = delay_tol[0]
    for i in range(1, order_count):
        if delay_tol[i] < delay_min:
            index = i
            delay_min = delay_tol[i]
            
    a = order[index].copy()
    b = order_origin.copy()
    if a == b:
        break

print(order_origin[0], end='')
for i in range(1, tasks_count):
    print(f',{order_origin[i]}', end='')
print(f';{delay_min}')
