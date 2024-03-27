order_count = job_cnt + 1

index = 0
order = []
order.append(init_seq)
while True:
    init_seq = order[index].copy()
    order = []
    order.append(init_seq.copy())
    for i in range(job_cnt):
        order.append(init_seq.copy())
        tmp = order[i+1][i]
        order[i+1][i] = order[i+1][(i+1) % job_cnt]
        order[i+1][(i+1) % job_cnt] = tmp

    delay_tol = [0] * order_count
    time = [0] * order_count
    for i in range(job_cnt):
        for j in range(order_count):
            time[j] += processing_times[order[j][i]-1]
            delay = time[j] - due_times[order[j][i]-1]
            if delay > 0:
                delay_tol[j] += delay

    index = 0
    delay_min = delay_tol[0]
    for i in range(1, order_count):
        if delay_tol[i] < delay_min:
            index = i
            delay_min = delay_tol[i]
            
    a = order[index].copy()
    b = init_seq.copy()
    if a == b:
        break

print(init_seq[0], end='')
for i in range(1, job_cnt):
    print(f',{init_seq[i]}', end='')
print(f';{delay_min}')
