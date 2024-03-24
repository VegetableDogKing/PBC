txt = input().split(",")
spots = int(txt[0])
capacity = int(txt[1])

num_people = 0
people = input().split(",")
for i in range(spots):
    people[i] = int(people[i])
    num_people += people[i]

distance = []
for i in range(spots+1):
    distance.append(input().split(","))
    for j in range(spots+1):
        distance[i][j] = int(distance[i][j])

bus = 0
length_tol = 0
while num_people != 0:
    start = 0
    bus += 1
    capacity_left = capacity
    while capacity_left > 0:
        next_stop = 0
        length_min = 20000
        onboard = 0
        for i in range(1, spots + 1):
            dest = (start + i) % (spots + 1)
            length = distance[start][dest]
            if dest != 0 and people[dest-1] != 0 and people[dest-1] <= capacity_left and length < length_min:
                next_stop = dest
                onboard = 1
                length_min = length
        if onboard == 1:
            capacity_left -= people[next_stop-1]
            num_people -= people[next_stop-1]
            people[next_stop-1] = 0
            length_tol += distance[start][next_stop]
            start = next_stop
        else:
            break
    length_tol += distance[start][0]

print(str(bus) + "," + str(length_tol))
