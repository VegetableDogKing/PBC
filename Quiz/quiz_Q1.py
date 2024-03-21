txt = input().split(",")
a = int(txt[0])
b = int(txt[1])
c = int(txt[2])

ans1 = a + b
ans2 = b + 2 * c
ans3 = a * c

max_ans = ans1
if ans2 > max_ans:
    max_ans = ans2
if ans3 > max_ans:
    max_ans = ans3
    
print(max_ans)