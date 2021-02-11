def count(sub, str):
    M = len(sub)
    N = len(str)
    res = 0

    for i in range(N):
        j = 0
        while j < M:
            if (str[i + j] != sub[j]):
                break
            j += 1

        if (j == M):
            res += 1
            j = 0
    return res


if __name__ == '__main__':
    str = input()
    sub = input()
    print(count(sub, str))
str=list(input())
sub=list(input())
x=len(str)
y=len(sub)
result=0
counter=True

while True:
    for i in range(x):
        if i==str:
            continue
        else:
            counter=False
    if counter:
        z=''
        for i in y:
            for j in range(x):
                if i==str[j]:
                    z+= str[j]
                    str[j]= None
                    break

        if z==sub:
            result=result+1
    else: break
print(result)
