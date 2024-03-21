#輸入各參數
#輸入紅玫瑰單價p_R
#輸入白玫瑰單價p_W
#輸入預算b
p_R = int(input())
p_W = int(input())
b = int(input())

#計算最大開心程度degree_max
degree_max = 0
for r in range(0, 101):
    for w in range(0, 76):
        if (r*p_R + w*p_W)<=b and r>=w*2:
            degree = (200-r)*r + (300-2*w)*w
            if degree>degree_max:
                degree_max = degree
                
print(degree_max)