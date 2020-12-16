v = []
v.append('3.4k')

v.append('321')
v.append('2,123')


for i, e in enumerate(v):
    if e[-1] == 'k':
        v[i] = float(e[:-1].replace(",", ""))*1000
    else:
        v[i]=float(e.replace(",", ""))
    print(v[i], type(v[i]))

# print(v)
