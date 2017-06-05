"""20 世纪（1901 年 1 月 1 日到 2000 年 12 月 31 日）一共有多少个星期日落在了当月的第一天？"""


def days_in_year(year):  # 每年的天数
    days = 365
    if year % 4 == 0 and year % 100 != 0:
        days += 1
    return days


start_day = 2  # 1901 第一天是星期二
count = 0

for year in range(1901, 2001):
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # 闰年二月加一
    if days_in_year(year) == 366:
        month[2] += 1

    for i in range(1, 13):
        # 下面这个if模块是计算本月开始是否周天
        if start_day == 0:
            count += 1
        # 每月天数对7的余数加到start_day里面，为了防止start_day超过7再余一次
        # 下面计算的是下一个月的start_day是否为周天
        days = month[i]
        start_day += days % 7
        start_day = start_day % 7

print('答案是： ' + str(count))
