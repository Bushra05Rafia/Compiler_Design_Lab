def count(str, sub):
    counter = True
    result = 0
    x = len(str)
    while True:
        if counter == True:
            findsub =''
            for i in sub:
                for j in range(x):
                    if i == str[j]:
                        print("i" ,i)
                        findsub += str[j]
                        print("findsub",findsub)
                        str[j] = ''
                        break
                if i not in str:
                    counter = False
            if sub == findsub:
                result = result + 1
                print("result",result)
        else: break
    return result

if __name__ == '__main__':
    print("Enter the String: ")
    str=list(input())
    print("Enter the SubString: ")
    sub=input()
    print("Final Count=", count(str,sub))