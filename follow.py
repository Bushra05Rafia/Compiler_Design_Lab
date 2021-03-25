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
                #print('string[i:]=', string[i:])
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
    return  first_


def follow(x):
    follow_ = set()
    prods = productions_dict.items()
    if x == start_with:
        follow_ = follow_ | {'$'}

    for i, j in prods:
        for alt in j:
            for char in alt:
                if char == x:
                    following_str = alt[alt.index(char) + 1:]

                    if following_str == '':
                        if i == x:
                            continue
                        else:
                            follow_ = follow_ | follow(i)
                    else:
                        follow_2 = first(following_str)

                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(i)
                        else:
                            follow_ = follow_ | follow_2
    return follow_



X=int(input("Terminals:"))
terminals = []
for i in range(X):
    terminals.append(input())

Y=int(input("Non terminals:"))
non_terminals = []
for i in range(Y):
    non_terminals.append(input())

start_with = input("Starting symbol: ")
Z = int(input("Productions: "))
productions = []
for _ in range(Z):
    productions.append(input())

productions_dict = {}
for i in non_terminals:
    productions_dict[i] = []

for i in productions:
    nonterm_to_prod = i.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for j in alternatives:
        productions_dict[nonterm_to_prod[0]].append(j)

FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

for i in non_terminals:
    FIRST[i] = FIRST[i] | first(i)

FOLLOW[start_with] = FOLLOW[start_with] | {'$'}
for i in non_terminals:
    FOLLOW[i] = FOLLOW[i] | follow(i)

for i in non_terminals:
    print(i,"=",  "Follow:", str(FOLLOW[i]))