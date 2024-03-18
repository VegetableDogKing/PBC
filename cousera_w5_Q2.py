while True:
    txt = input().split(" ")
    count = int(txt[0])
    radius = int(txt[2])
    amount = int(txt[1])
    length = radius * radius

    data = []
    for i in range(count):
        data.append(input().split(" "))
        for j in range(3):
            data[i][j] = float(data[i][j])
            
    distance = []
    for i in range(count):
        tmp = []
        for j in range(i+1, i+count):
            d = (data[i][0]-data[j%count][0]) * (data[i][0]-data[j%count][0]) + (data[i][1]-data[j%count][1]) * (data[i][1]-data[j%count][1])
            tmp.append(d)
        distance.append(tmp)

    total = 0
    covered = []
    for i in range(amount):
        people_max = 0
        index = 0
        for j in range(count):
            people = 0
            if j not in covered:
                people += data[j][2]
            for k in range(count-1):
                if (j+k+1)%count not in covered:
                    if distance[j][k] <= length:
                        people += data[(j+k+1)%count][2]
            if people > people_max:
                people_max = people
                index = j+1
        print(f'{index} ', end="")
        covered.append(index-1)
        total += people_max
        for l in range(count-1):
            if (index+l+1)%amount not in covered:
                if distance[index-1][l] <= length:
                    covered.append((index+l)%count)
    print(int(total))
