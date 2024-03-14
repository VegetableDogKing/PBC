tasks = int(input())
process_time = []
process_time = input().split(',')

deadline = []
deadline = input().split(',')

order = []
order = input().split(',')

for i in range(tasks):
    process_time[i] = int(process_time[i])
    deadline[i] = int(deadline[i])
    order[i] = int(order[i])
    
delay_tol = 0
time = 0
for i in range(tasks):
    time += process_time[order[i]-1]
    delay = time - deadline[order[i]-1]
    if delay > 0:
        delay_tol += delay
        
print(delay_tol)
