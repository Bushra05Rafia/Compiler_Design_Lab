counter = 0
def count (string, substring, x, counter):
    while(1):
        findsubstring = []
        for i in substring:
            for j in range(x):

                if string[j] == i:
                    findsubstring.append(i)
                    print("findsub=", findsubstring)
                    string[j] = []
                    break
                #print(string[j])

        if substring == findsubstring:
            #print(substring, findsubstring)
            counter += 1
            #print(result)

        else:
            break

    return counter

if __name__ == '__main__':
    print("String: ")
    string = list(input())
    print("SubString: ")
    substring = list(input())
    x = len(string)
    result= count(string, substring, x,counter)
    print("Count = ",result)