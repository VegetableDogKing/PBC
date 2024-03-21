num = int(input())
a3 = num // 1000
a2 = (num%1000) // 100
a1 = (num%100) // 10
a0 = (num%10)

y = 10*a2 + a1
print(y, end="")

if y*y == num:
    print(" 1")
else:
    print(" 0")