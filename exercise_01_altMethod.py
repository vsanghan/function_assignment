#assignment 1 : [12,4,55,7] => 55 #o/p max number

#alternate method, it will take first element and compare it with others. 

x = [12,4,55,7]

#def maxNum(num):
    a = num[0]
    for i in num[1:]:
        if i > a :
            a = i
            return (a)

print(maxNum(x))