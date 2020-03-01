#assignment 2 : [1,2,3,4,5,6,7] => 16 #sum of odd numbers

x = [1,2,3,4,5,6,7]

def addOdd(num):
    z = 0
    for i in num:
        if i%2 == 1:
            z = z + i
    return (z)

print (addOdd(x))