print("""例如 220 的真因子是 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 和 110; 因此 d(220) = 284.
 284 的真因子是 1, 2, 4, 71 和 142; 所以 d(284) = 220. 220和284是亲和数
 计算 10000 以下所有亲和数之和。""")

def d(n):
    num = 0
    # 真因子不算自己
    for i in range(1,n):
        if n % i == 0 :
            num += i
    return num

sum_num = 0
print('亲和数为：')
for i in range(1,10000):
    # i等于自己倒数的倒数，还不能等于自己才符合
    if i == d(d(i)) and i != d(i):
        sum_num +=  i
        print(i, end="/")
print('')
print('亲和数和为： ' +str(sum_num))
