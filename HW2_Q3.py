import math
#輸入各參數
#幸福花束r1 w1 y1 800元
#真心花束r2 w2 y2 1000元
#紅不小於k1
#白+黃不小於k2
#3紅+白不小於k3
#預算b
r1 = int(input())
w1 = int(input())
y1 = int(input())
r2 = int(input())
w2 = int(input())
y2 = int(input())
k1 = int(input())
k2 = int(input())
k3 = int(input())
b = int(input())

#利用迴圈運算有幾種策略strategies並且看那一個策略可行來算出最低價price_min
#用迴圈先固定真心花束的數量(從0到floor(b/1000))，再看剩餘的錢left可以買幾束幸福花束(從0到floor(b/800))
strategies = 0
price_min = 0
for count_1000 in range(0, math.floor(b/1000)+1):
    left = b - 1000*count_1000
    for count_800 in range(0, math.floor(left/800)+1):
        strategies = strategies + 1
        
        #判斷是否可行
        #計算出花朵數r_count, w_count, y_count並判斷是否可行
        r_count = r2*count_1000 + r1*count_800
        w_count = w2*count_1000 + w1*count_800
        y_count = y2*count_1000 + y1*count_800
        if r_count>=k1 or (w_count+y_count)>=k2 or (3*r_count+w_count)>=k3:
            #若可行則算出此次策略的價格price，若price_min=0代表目前沒有可行策略則price_min = price，若price_min!=0則比較price與price_min
            price = 1000*count_1000 + 800*count_800
            if price_min!=0 and price<price_min:
                price_min = price
            elif price_min==0:
                price_min = price
                
#若price_min為0代表沒有可行策略，輸出-1
print(f"{strategies},", end="")
if price_min==0:
    print(-1)
else:
    print(price_min)