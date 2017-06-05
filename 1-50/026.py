"""找出小于 1000 的数字 d，1/d 的十进制表示含有最长的循环圈"""


# 扩10取余
def len_is(x):
    b = []
    a = 10 % x
    while a not in (b):
        b.append(a)
        a = (a * 10) % x
    return len(b)


# 找最长
max_num = 0
max_len = 0
for d in range(1, 1000):
    if len_is(d) > max_len:
        max_len = len_is(d)
        max_num = d
print('答案是： ' + str(max_num))
