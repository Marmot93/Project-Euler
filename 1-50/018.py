"""找出从以下三角形的顶端走到底端的最大总和："""

data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data_list = [i.split(' ') for i in data.split('\n')]  # 数据清洗

# 从倒数第二排开始加后一排，取最大的那个，构成新数列
for i in range(len(data_list) - 2, -1, -1):  # 取倒数第二排
    for j in range(len(data_list[i])):  # 遍历最后一排
        # max（加自己下面 ，和右下边那个）
        data_list[i][j] = max(int(data_list[i][j]) + int(data_list[i + 1][j]),
                              int(data_list[i][j]) + int(data_list[i + 1][j + 1]))

        # print(max( data_list[i] ))

print('答案是：' + str(data_list[0][0]))
