txt = input().split(",")
r = int(txt[0])
w = int(txt[1])
y = int(txt[2])
k1 = int(txt[3])
k2 = int(txt[4])
k3 = int(txt[5])

ans1 = k1 // r
if k1%r != 0:
    ans1 += 1
    
ans2 = k2 // (w+y)
if k2%(w+y) != 0:
    ans2 += 1
    
ans3 = k3 // (3*r + w)
if k3%(3*r+w) != 0:
    ans3 += 1
    
max_ans = ans1
min_ans = ans1
if ans2 > max_ans:
    max_ans = ans2
if ans3 > max_ans:
    max_ans = ans3
    
if ans2 < min_ans:
    min_ans = ans2
if ans3 < min_ans:
    min_ans = ans3
    
print(str(min_ans) + "," + str(max_ans))
