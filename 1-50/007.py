"""前六个质数是 2, 3, 5, 7, 11 和 13，其中第 6 个是 13。
第 10001 个质数是多少？
 ----------------------------------------------------------------"""

from  math import sqrt


# 判断质数：从 2 直除到自己的平方根都除不尽就是质数，返回True
def prime_number(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 计数器，自己先验证一下第 2 个质数是 3
counter = 0
i = 1
while counter < 10001:
    i += 1
    if prime_number(i):
        counter += 1
print("答案是： " + str(i))
