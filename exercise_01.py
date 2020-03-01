#assignment 1 : [12,4,55,7] => 55 #o/p max number

def maxNum(num):
    a = 0
    for i in num:
        if i > a:
            a = i
    return (a)

x = [12,4,55,7]

print(maxNum(x))