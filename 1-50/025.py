print("""斐波那契数列中第一个包含 1000 位数字的项是第几项？""")


list_feb = [1, 1]
count = 2
while (True):
    n = list_feb[-1] + list_feb[-2]
    if len(str(n)) == 1000:
        print('答案是：' + str(count + 1))      #循环到这个的时候break但是计数还是得+1
        break
    else:
        list_feb.append(n)
        count +=1
