#assignment 3 : [1,2,3], ['a','b','c'] => [1,'a',2,'b',3,'c'] #placing it alternativley

x = [1,2,3]
y = ['a','b','c']

z = []
for i in x:
    z.append(i)
    d = 0
    for j in y:
        if z[d%2==1]==True:
            if j not in z : 
                z.append(j)
                d += 1
        else: 
            break
print(z)