#輸入各資料
#x_0為花束的基本價格
#x_1為紅玫瑰花一朵的價格
#x_2為白玫瑰花一朵的價格
#y_1為紅玫瑰花數量
#y_2為白玫瑰花數量
x_0 = int(input())
x_1 = int(input())
x_2 = int(input())
y_1 = int(input())
y_2 = int(input())

#計算花朵數量flowers_total
flowers_total = y_1 + y_2

#計算花束總價格price_total
price_total = x_0 + x_1*y_1 + x_2*y_2

#輸出
print(str(flowers_total) + "," + str(price_total))