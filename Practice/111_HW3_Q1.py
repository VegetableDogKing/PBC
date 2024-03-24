txt = input().split(",")
day = int(txt[0])
money = int(txt[1])
price = input().split(",")
for i in range(day):
    price[i] = int(price[i])

standard = input().split(",")
for i in range(2):
    standard[i] = int(standard[i])

stock = 0
left = money
for i in range(day - 1):
    if price[i] <= standard[0]:
        buy = left // 2 // price[i]
        stock += buy
        left -= buy * price[i]
    elif price[i] >= standard[1]:
        sell = stock // 2
        stock -= sell
        left += sell * price[i]

left += stock * price[day - 1]
print(left)
