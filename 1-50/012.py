print('问题：第一个拥有超过 500 个约数的三角形数是多少？')

from math import sqrt

def sanjiao(n):
    return (n * (n + 1)) // 2

count = 0
n = 1
while count <= 500:
    n += 1
    count = 1   #下面可能要减 先加一个，最后减
    for i in range(1, int(sqrt(sanjiao(n)))):
        if not sanjiao(n) % i:
            count += 2
    if int(sqrt(sanjiao(n))) == sqrt(sanjiao(n)) : # 刚好是平方数 减一
        count -= 1
print('答案是： '+ str(sanjiao(n)))
print('因数个数是： ' + str(count - 1))