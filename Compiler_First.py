terminals = ['+','*','i','(',')']
non_terminals = ['E','B','T','Y','F']
starting_symbol = ['E']
productions = ['E->TB', 'B->+TB/@', 'T->FY', 'Y->*FY/@', 'F->i/(E)']
productions_dict = {}
F = {}
for i in non_terminals:
    productions_dict[i] = []

for i in productions:
    equ = i.split("->")
    alternatives = equ[1].split("/")
    for j in alternatives:
        productions_dict[equ[0]].append(j)
print("productions_dict",productions_dict)

for i in non_terminals:
    F[i] = set()

def first(string):
    first_ = set()

    if string in non_terminals:
        cngstr = productions_dict[string]

        for i in cngstr:
            first_2 = first(i)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='@':
        first_ = {'@'}
    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                first_ = first_ | (first_2 - {'@'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2
    return first_

for i in non_terminals:
    F[i] = F[i] | first(i)

for i in non_terminals:
    print(i, "-First:", str(F[i]))
