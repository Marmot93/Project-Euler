"""从一个 2×2 网格的左上角开始，有 6 条（不允许往回走）通往右下角的路.'
20×20的网格有多少条路？"""


# 排列组合

def cnm(n, m):
    n_jiecheng = 1
    m_jiecheng = 1
    mn_jiecheng = 1
    for i in range(1, n + 1):
        n_jiecheng *= i
    for j in range(1, m + 1):
        m_jiecheng *= j
    for k in range(1, (m - n) + 1):
        mn_jiecheng *= k

    num = m_jiecheng // (n_jiecheng * mn_jiecheng)
    return num


print('答案是： ' + str(cnm(20, 40)) + ' 条路')
