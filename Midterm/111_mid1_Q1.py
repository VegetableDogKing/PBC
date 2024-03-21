num_Student = input().split(",")
num_Study = int(num_Student[0])
num_PBC = int(num_Student[1])

total_Study = 0
score_Study = input().split(",")
for i in range(num_Study):
    total_Study += int(score_Study[i])
avg_Study = total_Study / num_Study

total_PBC = 0
score_PBC = input().split(",")
for i in range(num_PBC):
    total_PBC += int(score_PBC[i])
avg_PBC = total_PBC / num_PBC

if avg_Study > avg_PBC:
    print(1)
elif avg_PBC > avg_Study:
    print(2)
else:
    print(0)
