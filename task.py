def count(str, sub):
    counter = True
    result = 0
    x = len(str)
    while True:
        if counter == True:
            findsub = ''
            for i in sub:
                for j in range(x):
                    if i == str[j]:
                        findsub += str[j]
                        str[j] = ''
                        break
                if i not in str:
                    counter = False
                    break

            if sub == findsub:
                result = result + 1
        else:
            break
    return result

print("Enter the String: ")
str=list(input())
print("Enter the SubString: ")
sub=input()
print(count(str,sub))