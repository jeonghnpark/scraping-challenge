a=[1,2,3,4]
print(a)
for i,s in enumerate(a):
    if s>0 :
        a[i]*=2
        print('i modified')

print(a)

s="djflsdjlfsjdfls"

i=0
while i<10:
    if '.' not in s:
        print('not in')
        i+=1
        continue
    else:
        print('in')
        break



