import re

num = []
oplist = ["+","-","*","/"]
op = []
value = input()
length = len(value)
indx = 0


num = re.findall(r"\d+", value)
len_num = len(num)


for i in range(length):
    if value[i] in oplist:
        op.append(value[i])
len_opt = len(op)


for i in range(len_num):
    num[i] = int(num[i])

for i in range(len_num-1):
    if op[i] == "+":
        num[i+1] += num[i]
    if op[i] == "-":
        num[i + 1] -= num[i]
    if op[i] == "*":
        num[i + 1] *= num[i]
    if op[i] == "/":
        num[i + 1] /= num[i]

print(num[i+1])