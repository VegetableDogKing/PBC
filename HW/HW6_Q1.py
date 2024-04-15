def store_order(file, number):
    ans = dict()
    file.readline()
    for i in range(number):
        line = file.readline().strip().split(',')
        if ans.get(line[0]) is not None:
            ans[line[0]] += int(line[3]) * int(line[4])
        else:
            ans[line[0]] = int(line[3]) * int(line[4])
    return ans


def commodity_order(file, number):
    ans = dict()
    file.readline()
    for i in range(number):
        line = file.readline().strip().split(',')
        if ans.get(line[2]) is not None:
            ans[line[2]] += 1
        else:
            ans[line[2]] = 1
    return ans


filename = input()
number = int(input())
type = input()

file = open(filename, 'r', encoding="utf-8")
if type == 'S':
    ans = store_order(file, number)
    sorted_ans = sorted(ans.items(), key=lambda x: (-x[1],len(x[0]),x[0]))
else:
    ans = commodity_order(file, number)
    sorted_ans = sorted(ans.items(), key=lambda x: (-x[1],int(x[0])))

print(sorted_ans)
for i in range(3):
    print(f'{sorted_ans[i][0]},{sorted_ans[i][1]}')
