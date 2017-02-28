print('问题：第一个拥有超过 500 个约数的三角形数是多少？')

from math import sqrt

def sanjiao(n):
    return (n * (n + 1)) // 2

count = 0
n = 1
while count <= 500:
    count = 1
    n += 1
    for i in range(1, int(sqrt(sanjiao(n)))):
        if not sanjiao(n) % i:
            count += 2

print('答案是： '+ str(sanjiao(n)))