''' write a function which will take three integers as input and returns the maximum integer amongst those three as the output '''

def maximum(a,b,c):
    if a > b and a > c:
        return (str(a)+' is biggest')
    elif b > a and b >c :
        return(str(b)+' is biggest')
    else :
        return (str(c)+' is biggest')

print (maximum(1,2,3))