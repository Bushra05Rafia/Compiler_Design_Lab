def concat(*str):
    result = ''
    for i in str:
        result = _concat(result, i)
    return result

def _concat(a, b):
    la = len(a)
    lb = len(b)
    for i in range(la):
        j = i
        k = 0
        while j < la and k < lb and a[j] == b[k]:
            j += 1
            k += 1
        if j == la:
            n = k
            break
    else:
        n = 0
    return a + b[n:]

if __name__ == '__main__':
    print(concat('ACTGA', 'TGAGTA', 'TATG','XYZ'))