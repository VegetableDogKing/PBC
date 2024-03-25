kinds = int(input())

red = input().split(",")
yellow = input().split(",")
white = input().split(",")
price = input().split(",")
for i in range(kinds):
    red[i] = int(red[i])
    yellow[i] = int(yellow[i])
    white[i] = int(white[i])
    price[i] = int(price[i])

red_standard = input().split(",")
yellow_standard = input().split(",")
white_standard = input().split(",")
for i in range(2):
    red_standard[i] = int(red_standard[i])
    yellow_standard[i] = int(yellow_standard[i])
    white_standard[i] = int(white_standard[i])

fit = 0
min_price = 5000
for i in range(kinds):
    if red[i] >= red_standard[1] and yellow[i] >= yellow_standard[1] and white[i] >= white_standard[1]:
        cur_price = price[i]
        fit = 1
        if cur_price < min_price:
            min_price = cur_price
    for j in range(i, kinds):
        if red[i] + red[j] >= red_standard[1] and yellow[i] + yellow[j] >= yellow_standard[1] and white[i] + white[j] >= white_standard[1]:
            cur_price = price[i] + price[j]
            fit = 1
            if cur_price < min_price:
                min_price = cur_price

if fit == 0:
    for i in range(kinds):
        if red[i] >= red_standard[0] and yellow[i] >= yellow_standard[0] and white[i] >= white_standard[0]:
            cur_price = price[i]
            fit = 1
            if cur_price < min_price:
                min_price = cur_price
        for j in range(i, kinds):
            if red[i] + red[j] >= red_standard[0] and yellow[i] + yellow[j] >= yellow_standard[0] and white[i] + white[j] >= white_standard[0]:
                cur_price = price[i] + price[j]
                fit = 1
                if cur_price < min_price:
                    min_price = cur_price

if fit == 0:
    min_price = 0
    for i in range(kinds):
        min_price += price[i]
print(min_price)
