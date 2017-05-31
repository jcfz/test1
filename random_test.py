import random


def get_dict_index(r, ls):
    start = 0
    end = 0
    zp = 0
    for l in ls:
        end += l
        if start < r <= end:
            zp = ls.index(l) + 1
        start += l
    return zp


lottery_probability = [0, 5, 60, 35, 0, 0]
for i in range(0,100000):
    r = random.randint(1, 99)
    zp = get_dict_index(r, lottery_probability)
    if zp==0:
        print r
        print 'zp=',zp
