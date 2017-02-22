print("""10 以下的质数的和是 2 + 3 + 5 + 7 = 17。
找出两百万以下所有质数的和
 ----------------------------------------------------------------""")
from math import sqrt

def prime_number(n):  #确定质数
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0 :
            return False
    return True

# 带3开始每次加 2 减少运算量，最后结果加上2和3即可
x = 3
aw = 5
while x < 2000000 :
    x += 2
    if prime_number(x) :
        aw += x

print(aw)