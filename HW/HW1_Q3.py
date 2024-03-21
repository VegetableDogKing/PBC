#輸入各資料
#至少r_0朵紅玫瑰和w_0朵白玫瑰
#開心花束由r_1朵紅玫瑰和w_1朵白玫瑰組成，價格p_1
#快樂花束由r_2朵紅玫瑰和w_2朵白玫瑰組成，價格p_2
r_0 = int(input())
w_0 = int(input())
r_1 = int(input())
w_1 = int(input())
p_1 = int(input())
r_2 = int(input())
w_2 = int(input())
p_2 = int(input())

#判斷是否有符合以及價格以及花朵數量
price_total = 0
flowers_total = 0
fit = False
if r_1>=r_0 and w_1>=w_0:
    flowers_total = r_1 + w_1
    price_total = p_1
    fit = True
elif r_2>=r_0 and w_2>=w_0:
    if (fit==True and p_2<p_1) or fit==False:
        flowers_total = r_2 + w_2
        price_total = p_2
        fit = True
        
if fit == False:
    flowers_total = r_1 + w_1 + r_2 + w_2
    price_total = p_1 + p_2

print(str(flowers_total) + "," + str(price_total))