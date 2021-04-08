def find_RE(str):
    #for range
    if str.startswith('[') and str.endswith(']'):
        x = str[1]
        y = str[3]
        result = []
        for i in range(ord(x), ord(y) + 1):
            result.append(chr(i))
        return result

    # for only a*/a+
    if str[0].isalpha() and len(str) == 2:

        if str.endswith('*'):
            result = []
            result.insert(0, '0')
            for i in range(1, 3):
                result.append(i * str[0])
            return result

        elif str.endswith('+'):
            result = []
            for i in range(1, 4):
                result.append(i * str[0])
            return result

    # for (ab)*
    if str.startswith('(') and str.endswith(')*'):
        x = str[1 : len(str) - 2]
        result = []
        result.insert(0, '0')
        for i in range(1, 3):
            result.append(i * x)
        return result

    # for (ab)+
    if str.startswith('(') and str.endswith(')+'):
        x = str[1 : len(str) - 2]
        result = []
        for i in range(1, 4):
            result.append(i * x)
        return result

    # for a*b
    if str[1] == '*':
        result = []
        result.insert(0, str[2])
        for i in range(1, 3):
            result.append((i * str[0]) + str[2])
        return result

    # for a+b
    if str[1] == '+':
        result = []
        for i in range(1, 4):
            result.append((i * str[0]) + str[2])
        return result

    # for ab*
    if str[2] == '*':
        result = []
        result.insert(0, str[1])
        for i in range(1, 3):
            result.append((i * str[1]) + str[0])
        return result

    # for ab+
    if str[2] == '+':
        result = []
        for i in range(1, 4):
            result.append((i * str[1]) + str[0])
        return result


if __name__ == '__main__':
    str = input()
    x= find_RE(str)
    print(x)