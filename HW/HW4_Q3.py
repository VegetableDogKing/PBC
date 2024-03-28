input_seq = input().split(",")
people_num = int(input_seq[0])
feedback_num = int(input_seq[1]) + 1

people_list = []
for i in range(people_num):
    people_list.append(i)

possibility = []
for i in range(people_num):
    possibility.append(input().split(","))
    for j in range(feedback_num):
        possibility[i][j] = int(possibility[i][j])

feedback_left = input().split(",")
feedback_left.insert(0, people_num)
for i in range(feedback_num):
    feedback_left[i] = int(feedback_left[i])

feedback = [0] * people_num
while len(people_list) != 0:
    max_possibility = 0
    max_left = 0
    min_index = feedback_num
    client = 0
    for i in people_list:
        for j in range(feedback_num):
            if feedback_left[j] > 0:
                if possibility[i][j] > max_possibility:
                    max_possibility = possibility[i][j]
                    max_left = feedback_left[j]
                    min_index = j
                    client = i
                elif possibility[i][j] == max_possibility:
                    if feedback_left[j] > max_left:
                        max_left = feedback_left[j]
                        min_index = j
                        client = i
                    elif feedback_left[j] == max_left:
                        if j < min_index:
                            min_index = j
                            client = i

    feedback_left[min_index] -= 1
    feedback[client] = min_index
    people_list.remove(int(client))

for i in range(people_num):
    if i == 0:
        print(feedback[i], end="")
    else:
        print(f",{feedback[i]}", end="")
