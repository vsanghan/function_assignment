#assignment 3 : [1,2,3], ['a','b','c'] => [1,'a',2,'b',3,'c'] #placing it alternativley

#alternat method, This will not affect if any of the give list has repetative elements.

x = [1,2,3]
y = ['a','b','c']

z = []
for i in range(len(x)):
    z.append(x[i])
    z.append(y[i])

print(z)