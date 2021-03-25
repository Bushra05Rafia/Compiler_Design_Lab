import sys
sys.setrecursionlimit(60)
def first(string):
    #print("first({})".format(string))
    first_ = set()
    if string in non_terminals: #str er 1st char ta capital
        cngstr = productions_dict[string] #then oi capital char r rule ta ke niye ashlam prod dic theke
        #print("cngstr",cngstr)

        for i in cngstr:
            first_2 = first(i)#recursive call
            #print("first_2",first_2)
            first_ = first_ |first_2 #agge jodi kono 1st peye thaki oita ke toh rakhboi first_ a tarpor or ar part ao khugbo fisrt
            #print("first_1",first_)

    elif string in terminals: # got a first small char at the beginning of that rule
        first_ = {string} #oitai oi equ ar jnno first
        #print("first_11", first_)

    elif string=='' or string=='@': # got nothing or effcilion from a equ at the beginning of that rule
        first_ = {'@'} #tokhon effcilion /null oi equ ar jnno first
        #print("first_111", first_)

    else:
        # S=Bda/Cb
        first_2 = first(string[0]) #like when
        print("first_22", first_2)
        #suppose first= {@ ,a}
        if '@' in first_2:
            i = 1
            #B ar jnno first -  @ ,a
            while '@' in first_2:
                print("inside while")
                first_ = first_ | (first_2 - {'@'})
                # first - a
                print("first_1111", first_)
                print('string[i:]=', string[i:])
                if string[1:] in terminals: #S=Bd/Cb akon B r jnno first ber kora sesh ,so then terminal pailam d
                    #S=Bd/Cb
                    first_ = first_ | {string[i:]} #first_= d acce akon
                    # S=d/Cb , d terminal paici acta so first akon d ar jnno kujhbo
                    print("first_11111", first_)
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}  # if no teminal found then again put the @ in first
                    print("first_11111", first_)
                    break
                first_2 = first(string[i:]) # Non - terminal ar jnno recursive call dibo abar
                print("first_11111", first_)
                first_ = first_ | first_2 - {'@'} #recursive call ar por abr eikhane ashlle @ baad diye dibo,
                # karon oi non-terminaler jnno first ber koreci
                print("first_11211", first_)
                i += 1
        else:
            #suppose first= {i ,a}
            first_ = first_ | first_2
            print("first_11311", first_)

    print("returning for first({})".format(string),first_)
    return first_


terminals = ['+', '*', 'i', '(', ')']
non_terminals = ['E', 'B', 'T', 'Y', 'F']
starting_symbol = ['E']
productions = ['E->TB', 'B->+TB/@', 'T->FY', 'Y->*FY/@', 'F->i/(E)']

#terminals = ['a', ' b', 'c', 'd']
#non_terminals = ['S', 'B', 'C']
#productions = ['S->Bd/Cb', 'B->aB/@', 'C->cC/@']
productions_dict = {}
F = {}
for i in non_terminals:
    productions_dict[i] = []

for i in productions:
    equ = i.split("->")
    alternatives = equ[1].split("/")
    for j in alternatives:
        productions_dict[equ[0]].append(j)
print("productions_dict", productions_dict)
print("alternatives", alternatives)
for i in non_terminals:
    F[i] = set()
for i in non_terminals:
    F[i] = F[i] | first(i)
    print("ABC", F[i],first(i))

for i in non_terminals:
    print(i, "-First:", str(F[i]))
