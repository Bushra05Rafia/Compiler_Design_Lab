terminals = []
non_terminals = []
equations = []
productions_dict = {}
FIRST = {}
FOLLOW = {}
for i in non_terminals:
    print("First",str(FIRST[i]), "Follow", str(FOLLOW[i]))

terminals_no = int(input("Enter no. of terminals: "))
#print("Enter the terminals :")
for _ in range(terminals_no):
    terminals.append(input())
#print("terminals", terminals)

non_terminals_no = int(input("Enter no. of non terminals: "))
#print("Enter the non terminals :")
for _ in range(non_terminals_no):
    non_terminals.append(input())
#print("non terminals", non_terminals)

starting_symbol = input("Starting symbol: ")


no_of_equations = int(input("Enter no of productions: "))
print("Enter the productions:")
for _ in range(no_of_equations):
    equations.append(input())
print("productions",equations)

for i in non_terminals:
    productions_dict[i] = []
print("productions_dict",productions_dict)

for i in equations:
    equ = i.split("->")
    print("Nonterm_to_prod", equ)
    alternatives = equ[1].split("/")
    print("alternatives", alternatives)
    for j in alternatives:
        productions_dict[equ[0]].append(j)
        print("productions_dict", productions_dict)


for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

#print("FIRST",FIRST)

def first(string):
    print("first({})".format(string))
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]
        print("alternatives",alternatives)

        for i in alternatives:
            first_2 = first(i)
            print("first_2",first_2)
            first_ = first_ |first_2
            print("first_1",first_)

    elif string in terminals:
        first_ = {string}
        print("first_11", first_)

    elif string=='' or string=='@':
        first_ = {'@'}
        print("first_111", first_)

    else:
        first_2 = first(string[0])
        print("first_22", first_2)
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                print("inside while")

                first_ = first_ | (first_2 - {'@'})
                print("first_1111", first_)
                print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    print("first_11111", first_)
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    print("first_11111", first_)
                    break
                first_2 = first(string[i:])
                print("first_11111", first_)
                first_ = first_ | first_2 - {'@'}
                print("first_11211", first_)
                i += 1
        else:
            first_ = first_ | first_2
            print("first_11311", first_)

    print("returning for first({})".format(string),first_)
    return  first_


for i in non_terminals:
    FIRST[i] = FIRST[i] | first(i)
    print(FIRST[i],first(i))


for i in non_terminals:
    print(i, "-First:", str(FIRST[i]))
