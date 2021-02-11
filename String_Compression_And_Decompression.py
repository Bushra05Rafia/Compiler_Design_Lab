y = input("Compressed :")
num = 0
length2 = len(y)

for j in range(length2):

    if y[j].isalpha():
        print(y[j], end=" ")

    if y[j].isdigit():
        num = int(y[j])

        for i in range(num-1):
            print(y[j-1], end=" ")


s = []
count = 1
val = input("Enter string:")
length = len(val)

for i in range(length-1):
    if val[i] == val[i+1]:
        count += 1

    if val[i] != val[i+1]:
        s.append(val[i])
        if count > 1:
            s.append(count)
            count = 1

        if i == length - 2:
            s.append(val[i+1])
            s.append(count)

    if(val[i]==val[i+1]) and (i==length-2):
        s.append(val[i])
        s.append(count)
print(s)