#def move (n,a,b,c):
#   if n == 1:
#       print(a,'--->',c)
#  else:
#        print(a,'--->',b)
#        move(n-1,b,a,c)
#        print(b,'--->',c)
#move(3,'A','B','C')

def trim(s):
    i = 0
    while(1):
        if(s!='' and s[i] == ' '):
            s=s[i+1:]
        else :
            break
    i = -1
    while(1):
        if(s!='' and s[i] == ' '):
            s=s[:i]
        else:
            break
    print(s)
    return s
   

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

def findMinAndMax(L):
    if (L == []):
        return None, None
    max = L[0]
    min = L[0]
    for x in L:
        if(x > max):
            max = x
        if (x < min):
            min = x
    return min ,max

if findMinAndMax([]) != (None, None):
    print(findMinAndMax([]))
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




