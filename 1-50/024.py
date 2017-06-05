"""0, 1, 2, 3, 4, 5, 6, 7, 8, 9 的第 100 万个字典排列是什么"""

import itertools

count = 0
for i in list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
    count += 1
    if count == 1000000:
        print(i)
    else:
        continue

        # 参考廖学峰老师的 itertools
