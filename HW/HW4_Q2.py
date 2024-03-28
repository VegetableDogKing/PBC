#輸入客戶人數people以及優惠數目feedback_num
input_seq = input().split(",")
people = int(input_seq[0])
feedback_num = int(input_seq[1]) + 1

#輸入所有客戶每個優惠的機率
possibility = []
for i in range(people):
    possibility.append(input().split(","))
    for j in range(feedback_num):
        possibility[i][j] = int(possibility[i][j])

#輸入每個優惠剩餘人數
feedback_left = input().split(",")
feedback_left.insert(0, people)
for i in range(feedback_num):
    feedback_left[i] = int(feedback_left[i])

#輸入每個客戶可不可以被發送邀請
able = input().split(",")
for i in range(people):
    able[i] = int(able[i])

max_possibility = 0
max_left = 0
min_index = feedback_num
client = 0
for i in range(people):
    #如果可以被發送邀請再看
    if able[i] == 0:
        for j in range(feedback_num):
            #如果當前優惠還有剩餘人數再看
            if feedback_left[j] > 0:
                #如果機率比較大就換成當前方案
                if possibility[i][j] > max_possibility:
                    max_possibility = possibility[i][j]
                    max_left = feedback_left[j]
                    min_index = j
                    client = i
                #如果機率一樣就以剩餘人數判斷
                elif possibility[i][j] == max_possibility:
                    if feedback_left[j] > max_left:
                        max_left = feedback_left[j]
                        min_index = j
                        client = i
                    #如果剩餘人數又一樣就以編號大小判斷
                    elif feedback_left[j] == max_left:
                        if j < min_index:
                            min_index = j
                            client = i

print(str(client + 1) + "," + str(min_index))
