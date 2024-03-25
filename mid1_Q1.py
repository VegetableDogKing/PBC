num_string = input().split(",")
num1 = int(num_string[0])
num2 = int(num_string[1])
num3 = int(num_string[2])

if num1 * num2 == num3:
    print(num3)
elif num1 * num3 == num2:
    print(num2)
elif num2 * num3 == num1:
    print(num1)
else:
    print(num1 * num2 * num3)
