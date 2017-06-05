"""2520 是最小的能被 1-10 中每个数字整除的正整数。
最小的能被 1-20 中每个数整除的正整数是多少？
"""


# 逐项求解 求1~20 的最小公倍数

def gcd(x, y):  # 最大公约数
    max_i = 1
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0 and i > max_i:
            max_i = i
    return max_i


def lcm(a, b):  # a 和 b 的最小公倍数
    return (a * b) / gcd(a, b)


n = 3
num = 2
while n <= 20:
    num = lcm(num, n)  # 最小公倍数储存在 m 中
    n += 1  # 逐项求最小公倍数

print('答案是：' + str(num))
