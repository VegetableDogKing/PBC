num_Tasks = int(input())
finished = input().split(",")
deadline = input().split(",")
for i in range(num_Tasks):
    finished[i] = int(finished[i])
    deadline[i] = int(deadline[i])

for i in range(1, num_Tasks):
    for j in range(i-1, 0, -1):
        