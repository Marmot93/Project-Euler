"""找出前一百个自然数的平方和与和平方的差
"""
# 平方的和 - 和的平方
print('答案是： ' +
      str(sum([i ** 2 for i in range(1, 101)]) - sum(range(1, 101)) ** 2))
