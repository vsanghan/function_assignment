#assignment 4 : [1,2,3], ['a','b','c','d','e'] => [1,'a',2,'b',3,'c','d','e']

x = [1,2,3]
y = ['a','b','c','d','e']

z = []
for i in y:
    z.append(i)
    for j in x:
        if j not in z : 
            z.append(j)
            break
print(z)