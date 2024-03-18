num = input().split(" ")
for i in range(len(num)):
    num[i] = int(num[i])

txt = input().split()
y = int(txt[0])
z = int(txt[1])

now = 0
for i in range(len(num)):
    if num[now] == y:
        num.remove(y)
    else:
        now += 1

if z == 1:
    print(num[0], end="")
    for i in range(1, len(num)):
        print(f' {num[i]}', end="")
else:
    print(num[-1], end="")
    for i in range(1, len(num)):
        print(f' {num[-1-i]}', end="")
