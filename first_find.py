def callfirst(string):
    first = set()
    if string in non_terminals:
        cngstr = productions_dict[string]

        for i in cngstr:
            cng_first = callfirst(i)
            first = first | cng_first

    elif string in terminals:
        first = {string}

    elif string == '' or string == '@':
        first = {'@'}

    else:
        first_2 = callfirst(string[0]) #S=Bda/Cb ,B- first {@ ,a}
        if '@' in first_2:
            i = 1
            while '@' in first_2:

                first = first | (first_2 - {'@'}) #now B- first {a}
                if string[i: ] in terminals: # Now for this rule, S=Bda/Cb
                    # will find first for d terminal, [1: ] because already B ar jnno first peye geci
                    first = first | {string[i: ]}
                    break

                elif string[i: ] == ' ': #if S=B then will put @ at the end of the first
                    first = first | {'@'}
                    break

                first_2 = callfirst(string[i: ])# if no space/ terminal found
                #so its non terminal , will eliminate @ and find first for that non-terminal
                first = first | first_2 - {'@'}
                i += 1
        else:
            first = first | first_2

    return first



x = int(input("Enter no. of terminals: "))
terminals = []
print("Enter the terminals :")
for i in range(x):
    terminals.append(input())


y = int(input("Enter no. of non terminals: "))
non_terminals = []
print("Enter the non terminals :")
for i in range(y):
    non_terminals.append(input())


z = int(input("Enter no of productions: "))
productions = []
print("Enter the productions:")
for i in range(z):
    productions.append(input())


starting_symbol = input("Starting symbol: ")
productions_dict = {}
for i in non_terminals:
    productions_dict[i] = []


for i in productions:
    rule = i.split("->")
    alternatives = rule[1].split("/")
    for j in alternatives:
        productions_dict[rule[0]].append(j)
print("productions_dict", productions_dict)

Find_first = {}
for i in non_terminals:
    Find_first[i] = set()

for i in non_terminals:
    Find_first[i] = Find_first[i] | callfirst(i)

for i in non_terminals:
    print(i, ":", str(Find_first[i]))
