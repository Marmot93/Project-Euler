print(""" 斐波那契数列中的每一项被定义为前两项之和。从 1 和 2 开始，斐波那契数列的前十项为：
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
考虑斐波那契数列中数值不超过 4 百万的项，找出这些项中值为偶数的项之和。
 ----------------------------------------------------""")

#斐波拉契数列表
list_feb = [1, 2]
while (True):
    n = list_feb[-1] + list_feb[-2]
    if n > 4000000:
        break
    else:
        list_feb.append(n)

#取出偶数并相加
aw = 0
for x in list_feb:
    if x%2 == 0:
        aw += x

print("答案是： " + str(aw))
print("PS小于四百万的斐波拉契数列列表为：" + str(list_feb))
