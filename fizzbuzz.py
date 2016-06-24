for x in range(100):
    print 'fizz'[x%3*4::]+'buzz'[x%5*4::]or x
    print x,x%3,x%3*4,'fizz'[x%3*4:]
print '-------------------------------------'
for x in range(100):
    print x%3/2*'fizz'+x%5/4*'buzz' or x+1

print '-','fiza'[::2]
