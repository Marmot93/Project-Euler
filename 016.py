print("""2的1000次方各位数之和""")

# 送分题，一行代码解决问题
num = sum([int(i) for i in str(2 ** 1000) ])
print('答案是： ' + str(num))