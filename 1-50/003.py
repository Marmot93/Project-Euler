"""问题： 13195 的质数因子有 5, 7, 13 和 29。
600851475143 的最大质数因子是多少？
"""


# 数字除以2，若能被整除，取结果继续除以 i = 2，若不能则除以 i+1：
# 依序递增，直到被自己除，此时的数字即为所求的最大质因子。

def zhiyinzi(x):
    i = 2
    while x != 1:  # x 不等于 1
        if x % i == 0:  # 能除尽2
            x = x / i  # 继续除
            zhiyinzi = i  # 得到最大质因子
        else:
            i += 1  # 除不尽就 +1
    return zhiyinzi


print("答案是： " + str(zhiyinzi(600851475143)))
