import math
#輸入各參數
#r朵紅玫瑰
#w朵白玫瑰
#y朵黃玫瑰
#紅玫瑰不小於k1
#白玫瑰+黃玫瑰不小於k2
#紅玫瑰的三倍+白玫瑰不小於k3
r = int(input())
w = int(input())
y = int(input())
k1 = int(input())
k2 = int(input())
k3 = int(input())

#計算每一條件最少需要幾束必且取最小amount
amount = 0
#amount_1
if r>0:
    amount_1 = math.ceil(k1/r)
    amount = amount_1

#amount_2
if (w+y)>0:
    amount_2 = math.ceil(k2/(w+y))
    if amount == 0:
        amount = amount_2
    if amount_2<amount:
        amount = amount_2
    
#amount_3
if (3*r+w)>0:
    amount_3 = math.ceil(k3/(3*r+w))
    if amount == 0:
        amount = amount_3
    if amount_3<amount:
        amount = amount_3
    
print(amount)