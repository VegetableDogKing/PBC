a = int(input())

change = 1000-a

c_500 = change // 500
change = change%500

c_100 = change // 100
change = change%100

c_50 = change // 50
change = change%50

c_10 = change // 10
change = change%10

c_5 = change // 5
change = change%5

c_1 = change // 1
change = change%1

something = False

if c_500!=0:
    print(f"500, {c_500}", end="")
    something = True
if c_100!=0:
    if something == True:
        print("; ", end="")
    print(f"100, {c_100}", end="")
    something = True
if c_50!=0:
    if something == True:
        print("; ", end="")
    print(f"50, {c_50}", end="")
    something = True
if c_10!=0:
    if something == True:
        print("; ", end="")
    print(f"10, {c_10}", end="")
    something = True
if c_5!=0:
    if something == True:
        print("; ", end="")
    print(f"5, {c_5}", end="")
    something = True
if c_1!=0:
    if something == True:
        print("; ", end="")
    print(f"1, {c_1}", end="")
    something = True