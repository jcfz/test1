
f = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]
def age(s):
    return s['age']

ff = sorted(f,key = age)
print ff

f2 = sorted(f,key = lambda x:x['age'])

print f2
