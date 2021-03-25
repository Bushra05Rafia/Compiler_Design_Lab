def callfirst(string):
    first = set()
    if string in non_terminals:
        cngstr = productions_dict[string]

        for i in cngstr:
            first_1 = callfirst(i)
            first = first | first_1

    elif string in terminals:
        first = {string}

    elif string == '' or string == '#':
        first = {'#'}

    else:
        i = 0
        first_2 = callfirst(string[i])
        i += 1
        first = first | first_2

    return first


terminals = ['+', '*', 'i', '(', ')']
non_terminals = ['E', 'B', 'T', 'Y', 'F']
grammers = ['E=TB', 'B=+TB|#', 'T=FY', 'Y=*FY|#', 'F=i|(E)']

productions_dict = {}
for i in non_terminals:
    productions_dict[i] = []

for i in grammers:
    rule = i.split("=")
    alternatives = rule[1].split("|")
    for j in alternatives:
        productions_dict[rule[0]].append(j)
print("productions_dict", productions_dict)

Find_first = {}
for i in non_terminals:
    Find_first[i] = set()

for i in non_terminals:
    Find_first[i] = Find_first[i] | callfirst(i)

for i in non_terminals:
    print(i, "=", str(Find_first[i]))
