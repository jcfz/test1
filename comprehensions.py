# -*- coding:utf-8 -*-
#推导式 list comprehensions
#
num = [1,4,-5,10,-7,2,3,-1]
filter_and_squared=[]

for number in num:
    if number>0:
        filter_and_squared.append(number**2)
print filter_and_squared
#list comprehensions
filter_and_squared_lambda=map(lambda x:x**2,filter(lambda x:x>0,num))
print filter_and_squared_lambda

filter_and_squared_list=[x**2 for x in num if x>0]
print filter_and_squared_list

filter_and_squared_list=(x**2 for x in num if x>0)
print filter_and_squared_list

for item in filter_and_squared_list:
    print item
#
def square_generator(optional_parameter):
    return (x**2 for x in num if x>optional_parameter)
print square_generator(0)
