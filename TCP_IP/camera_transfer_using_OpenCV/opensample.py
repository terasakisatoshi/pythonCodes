f=open("sample.txt",'r')
lines=f.readlines()
f.close()

for line in lines:
    print line,
print 