print("""算出 100! 的各位之和""")

# 递归
def n_jie(n):
    if n == 1 :
        return 1
    else:
        return n * n_jie(n - 1)

num = sum([int(i) for i in str(n_jie(100))])

print(num)