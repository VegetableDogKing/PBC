def store_order(file):
    ans = dict()
    for lines in file:
        line = lines.split(',')
        if ans.get(line[0]) is not None:
            ans[line[0]] += line[3] * line[4]
        else:
            ans[line[0]] = line[3] * line[4]
    return ans


def commodity_order(file):
    

filename = input()
number = int(input())
type = input()

file = open(filename, 'r', encoding="utf-8")
if type == 'S':
    ans = store_order(file)
else:
    ans = commodity_order(file)


