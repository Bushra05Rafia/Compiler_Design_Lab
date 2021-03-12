n = int(input())
string = []
for _ in range(n):
    string.append(input())
print(string)
count = start = 0
while True:
    start = string.find(string[0], string[1]) + 1
    if start > 0:
        count+=1
    else:
        return count