#輸入各資料
#x_0為花束的基本價格
#x_1為紅玫瑰花一朵的價格
#x_2為白玫瑰花一朵的價格
#y_1為紅玫瑰花數量
#y_2為白玫瑰花數量
#k_1為第一個折扣門檻價格
#k_2為第二個折扣門檻價格
#b_1及b_2為總價區間
x_0 = int(input())
x_1 = int(input())
x_2 = int(input())
y_1 = int(input())
y_2 = int(input())
k_1 = int(input())
k_2 = int(input())
b_1 = int(input())
b_2 = int(input())

#計算花束總價格price_total
price_total = x_0 + x_1*y_1 + x_2*y_2

#計算花朵數量flowers_total並判斷是否有超過門檻
flowers_total = y_1 + y_2

#計算活動一
if price_total >= k_1:
    flowers_total += 2
if price_total >= k_2:
    flowers_total += 3
    
#計算活動二
if price_total>b_1 and price_total<=b_2:
    price_total = b_1 

#輸出
print(str(flowers_total) + "," + str(price_total))
