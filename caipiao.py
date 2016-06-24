# -*- coding:utf-8 -*-
import itertools
__author__ = 'john'

iterable = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32

num_list = list(itertools.combinations(iterable,6))
l = len(num_list)
for n in num_list:
    if (n[5]-n[4]==1 and n[4]-n[3]==1 and n[3]-n[2]==1 and n[2]-n[1]==1) or(n[4]-n[3]==1 and n[3]-n[2]==1 and n[2]-n[1]==1 and n[1]-n[0]==1):
        l=l-1
print l


