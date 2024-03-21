txt = input().split(",")
num_class = int(txt[0])
stantard = int(txt[1])
num_Student = input().split(",")
num_filled = input().split(",")

rate = []
for i in range(num_class):
    rate_each = int(num_filled[i]) * 100 / int(num_Student[i])
    rate.append(rate_each)

score_max = -1
avg_max = -1
class_max = 0
judge = 0
for i in range(num_class):
    score_each = input().split(",")
    sum = 0
    if rate[i] >= stantard:
        judge = 1
        for j in range(len(score_each)):
            if int(score_each[j]) > 0:
                sum += int(score_each[j])
        avg = sum / int(num_filled[i])
        if avg > avg_max:
            avg_max = avg
            score_max = sum
            class_max = i

if judge == 0:
    print(-1)
else:
    print(class_max+1, end="")
    print("," + num_Student[class_max] + "," + str(score_max))
