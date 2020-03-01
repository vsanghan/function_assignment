# Biggest number from the list. 

li = [5,7,15,42,12,45,78,25,86,68,75,214,587,5358,214,5684,524,2336,885,2563]

def greatest(a):
    num = 0
    for i in a:
        if i > num :
            num = i
    return (num)         
        
print (greatest(li))