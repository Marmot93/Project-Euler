"""将名字列表按照字母排序后， COLIN 这个名字是列表中的第 938 个，它的字母值是 3   15   12   9   14 = 53
所以 COLIN 这个名字的得分就是 938 × 53 = 49714.
文件中所有名字的得分总和是多少？
"""

# 读文件，大写/小写 排序，这里注释了大写版本
with open('022_data.txt', 'r') as f:
    names = f.read().split(",")
    # names = sorted([n.replace('"','').upper() for n in names])
    names = sorted([n.replace('"', '').lower() for n in names])


# ASCII码自己百度一下就可以了
def mark(a):
    # return int(ord(a) - 64)
    return int(ord(a) - 96)


sum_mark = 0
for i, name in enumerate(names):
    name_mark = sum([mark(i) for i in name])
    sum_mark += name_mark * (i + 1)
print('答案是： ' + str(sum_mark))
