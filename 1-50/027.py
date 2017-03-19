print("""对于能够为从 0 开始的连续的 n 产生最多数量的质数的二次公式，找出该公式的系数乘积。""")
from  math import sqrt

# 判断质数：从 2 直除到自己的平方根都除不尽就是质数，返回True
# 取个绝对值
def prime(n):
    for i in range(2, int(sqrt(abs(n))) + 1):
        if n % i == 0 :
            return False
    return True

primes = [x for x in range(2,1001) if prime(x)]
# b必须是质数
max_len = 2
ji = 0
for b in primes:
    for a in [x-b-1 for x in primes]:
        n = 2
        while True:
            if not prime(n * n + a * n + b):
                break
            n += 1
        if n > max_len:
            max_len = n
            ji = a*b

print('答案是： ' + str(ji))