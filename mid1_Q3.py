txt = input().split(",")
count = int(txt[0])
standard = int(txt[1])

number = input().split(",")
for i in range(count):
    number[i] = int(number[i])

fit = 0
for i in range(count):
    for j in range(i + 1, count):
        if number[i] * number[j] == standard:
            fit += 1

print(fit)
