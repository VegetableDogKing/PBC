txt = input().split(",")
menu = int(txt[0])
standard = int(txt[1])
price = input().split(",")
buy = input().split(",")
total = 0
for i in range(menu):
    price[i] = int(price[i])
    buy[i] = int(buy[i])
    total += price[i] * buy[i]

coupon = total // standard

print(f'{total},{coupon}')