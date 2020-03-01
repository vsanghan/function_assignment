#assignment 5 : [1,2,3,4,5], ['a','b','c'] => [1,'a',2,'b',3,'c',4,5]

x = [1,2,3]
y = ['a','b','c','d','e']

z = []
for i in y:
    z.append(i)
    d = 0
    for j in x:
        if z[d%2==1]==True:
            if j not in z : 
                z.append(j)
                d += 1
        else: 
            break
print(z)