print("""问题：求1000000以下的起始数字中，使克拉茨序列最长的那个。'
    n → n/2 (n 是偶数)
    n → 3n + 1 (n 是奇数)""")


# 长度函数
def length(num):
    count = 0       #计数
    while num != 1:
        if num % 2 == 0:
            num //= 2
            count += 1
        else:
            num = (num * 3) + 1
            count += 1

    return int(count+1)



i = 500000
max_len = 1
while i <= 1000000:
    i += 1
    if length(i) > max_len:
        max_len = length(i)
        max_num = i

# 效率一样
# for i in range(500000,1000000):
#     if length(i) > max_len:
#         max_len = length(i)
#         max_num = i

print('答案是：'+ str(max_num) , end='\n'
                                 '长度是： '+str(max_len))
