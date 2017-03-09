print("""如果一个数的所有真因子之和等于这个数，那么这个数被称为完全数。
例如，28 的所有真因子之和为 1   2   4   7   14 = 28，所以 28 是一个完全数。
如果一个数的所有真因子之和小于这个数，称其为不足数，如果大于这个数，称其为过剩数。
12 是最小的过剩数，1   2   3   4   6 = 16。因此最小的能够写成两个过剩数之和的数字是 24
可以证明，所有大于 28123 的数字都可以被写成两个过剩数之和。
问题：找出所有不能表示为两个过剩数之和的正整数之和。
""")

def abundant(n):
    num = 1
    for i in range(2,int(n / 2) + 1):
        if n % i == 0 :
            num += (i + n % i)
    if num > n :
        return True
    else:
        return False

abunants = [i for i in range(1,28124) if abundant(i)]
add_two = [x + y for x in abunants for y in abunants]

sum_num = 0
for i in range(1,28124):
    if not i in add_two:
        sum_num +=i
print(sum_num)
