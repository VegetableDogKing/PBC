import math
# 輸入各參數
# 幸福花束r1 white_happiness yellow_happiness 800元
# 真心花束r2 white_sincere yellow_sincere 1000元
# 紅不小於k1
# 白+黃不小於k2
# 3紅+白不小於k3
# 預算b
red_happiness = int(input())
white_happiness = int(input())
yellow_happiness = int(input())
red_sincere = int(input())
white_sincere = int(input())
yellow_sincere = int(input())
condition1 = int(input())
condition2 = int(input())
condition3 = int(input())
budget = int(input())

# 利用迴圈運算有幾種策略strategies並且看那一個策略可行來算出最低價price_min
# 用迴圈先固定真心花束的數量(從0到floor(budget/1000))，再看剩餘的錢left可以買幾束幸福花束(從0到floor(budget/800))
strategies = 0
price_min = 0
for count_1000 in range(0, math.floor(budget/1000)+1):
    left = budget - 1000*count_1000
    for count_800 in range(0, math.floor(left/800)+1):
        strategies = strategies + 1

        # 判斷是否可行
        # 計算出花朵數r_count, w_count, y_count並判斷是否可行
        r_count = red_sincere*count_1000 + red_happiness*count_800
        w_count = white_sincere*count_1000 + white_happiness*count_800
        y_count = yellow_sincere*count_1000 + yellow_happiness*count_800
        if r_count >= condition1 or (w_count+y_count) >= condition2 or \
                (3*r_count+w_count) >= condition3:
            # 若可行則算出此次策略的價格price，若price_min=0代表目前沒有可行策略則price_min = price
            # 若price_min!=0則比較price與price_min
            price = 1000*count_1000 + 800*count_800
            if price_min != 0 and price < price_min:
                price_min = price
            elif price_min == 0:
                price_min = price

# 若price_min為0代表沒有可行策略，輸出-1
print(f"{strategies},", end="")
if price_min == 0:
    print(-1)
else:
    print(price_min)
