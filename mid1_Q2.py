txt = input().split(",")
people = int(txt[0])
experience_standard = int(txt[1])
professionalism_standard = int(txt[2])
sum_standard = int(txt[3])

experience_info = input().split(",")
professionalism_info = input().split(",")
for i in range(people):
    experience_info[i] = int(experience_info[i])
    professionalism_info[i] = int(professionalism_info[i])

fit = 0
for i in range(people):
    if experience_info[i] >= experience_standard and professionalism_info[i] >= professionalism_standard:
        if fit == 1:
            print("," + str(i + 1), end="")
        else:
            print(str(i + 1), end="")
        fit = 1

if fit == 0:
    for i in range(people):
        if experience_info[i] + professionalism_info[i] >= sum_standard:
            if fit == 1:
                print("," + str(i + 1), end="")
            else:
                print(str(i + 1), end="")
            fit = 1

if fit == 0:
    print(0)
