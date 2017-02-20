print("""2520 是最小的能被 1-10 中每个数字整除的正整数。
最小的能被 1-20 中每个数整除的正整数是多少？
------------------------------------------------""")

import math
def lcm(a,b):
        return a * b // math.gcd(a,b)

n = 3
num = 2
while n <= 20:
        num = lcm(num,n)
        n += 1
print('答案是：' + str(num))