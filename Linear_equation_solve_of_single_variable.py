def isOperand(c):
    return (c >= '0' and c <= '9');


def value(c):
    return ord(c) - ord('0');

def evaluate(exp):
    len1 = len(exp);
    if (len1 == 0):
        return -1;

    res = value(exp[0]);
    for i in range(1, len1, 2):
        opr = exp[i];
        opd = exp[i + 1];


        if (isOperand(opd) == False):
            return -1;
        if (opr == '+'):
            res += value(opd);
        elif (opr == '-'):
            res -= int(value(opd));
        elif (opr == '*'):
            res *= int(value(opd));
        elif (opr == '/'):
            res /= int(value(opd));

        else:
            return -1;

    return res;

#print( ord('9')- ord('0'))

expr1= input("Enter eqation: ")
result = evaluate(expr1);

if (result == -1):
    print(expr1, "is Invalid")
else:
    print(int(result))
