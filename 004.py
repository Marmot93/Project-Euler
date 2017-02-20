print("""一个回文数指的是从左向右和从右向左读都一样的数字。
最大的由两个两位数乘积构成的回文数是 9009 = 91 * 99。
找出最大的有由个三位数乘积构成的回文数。
---------------------------------------------------""")

# 反向取乘积，换成字符串，反向分片,若相等得解,加入列表，取max

list_huiwen = []  #回文数列表
for x in range(999,100,-1):
    for y in range(999, 100, -1):
        num = str(x * y)
        num_1 = num[::-1]
        if num == num_1:   #判定字符串相等
            list_huiwen.append(int(num))

print("答案是： " + str(max(list_huiwen)) )

print("""
方法二：一行代码解
--------------------------------------------""")
num = (max([i*j for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1]]))
print("答案是： " + str(num))