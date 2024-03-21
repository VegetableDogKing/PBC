txt = input().split(",")
num_station, capacity = int(txt[0]), int(txt[1])

waiting = input().split(",")
for i in range(num_station):
    waiting[i] = int(waiting[i])

count = 0
while waiting[num_station-1] > 0:
    if i != 0:
        print()
    remain = capacity
    for i in range(num_station):
        if waiting[i] == 0 or remain == 0:
            if i == num_station-1:
                print("0", end="")
            else:
                print("0,", end="")
        else:
            if waiting[i] > remain:
                if i == num_station-1:
                    print(f'{remain}', end="")
                else:
                    print(f'{remain},', end="")
                waiting[i] -= remain
                remain = 0
            else:
                if i == num_station-1:
                    print(f'{waiting[i]}', end="")
                else:
                    print(f'{waiting[i]},', end="")
                remain -= waiting[i]
                waiting[i] = 0
    i += 1
