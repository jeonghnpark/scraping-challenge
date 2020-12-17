
s="hello.com,   youtube.com "
s2=s.strip().split(',')
l=list()
for e in s2:
    l.append(e.strip())

print(l)


l=list()
for e in s2:
    l.append(e.strip())

l

l2=[y.strip() for y in s.strip().split(',')]
l2