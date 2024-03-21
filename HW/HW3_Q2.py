tasks = input().split(',')
tasks_count = int(tasks[0])
order_count = int(tasks[1])

process_time = []
process_time = input().split(',')

deadline = []
deadline = input().split(',')

order = []
for i in range(order_count):
    order.append(input().split(','))
    for j in range(tasks_count):
        order[i][j] = int(order[i][j])

for i in range(tasks_count):
    process_time[i] = int(process_time[i])
    deadline[i] = int(deadline[i])
    
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
        
print(f'{index+1},{delay_min}')
