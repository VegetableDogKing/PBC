# 輸入工作數量tasks_count
# 順序數量為工作數量+1（原始的+相鄰的）
tasks_count = int(input())
order_count = tasks_count + 1

# 存入處理時間process_time，完成期限deadline，原始順序order_origin到list裡
process_time = input().split(',')
deadline = input().split(',')
order_origin = input().split(',')

# 將所有list裡的elements轉為int
for i in range(tasks_count):
    process_time[i] = int(process_time[i])
    deadline[i] = int(deadline[i])
    order_origin[i] = int(order_origin[i])

# 製作包含原始順序以及相鄰順序的二維list order
# 方式為將第一個與第二個交換，第二與第三交換.....
# 最後一個要與第一個交換，因此用取餘數的方式
order = []
order.append(order_origin.copy())
for i in range(tasks_count):
    order.append(order_origin.copy())
    tmp = order[i+1][i]
    order[i+1][i] = order[i+1][(i+1) % tasks_count]
    order[i+1][(i+1) % tasks_count] = tmp

# 計算每一個順序的時間存入time以及延遲存入delay
delay_tol = [0] * order_count
time = [0] * order_count
for i in range(tasks_count):
    for j in range(order_count):
        time[j] += process_time[order[j][i]-1]
        delay = time[j] - deadline[order[j][i]-1]
        if delay > 0:
            delay_tol[j] += delay

# 比較每一個delay選出最小
delay_min = delay_tol[0]
for i in range(1, order_count):
    if delay_tol[i] < delay_min:
        delay_min = delay_tol[i]

print(delay_min)
