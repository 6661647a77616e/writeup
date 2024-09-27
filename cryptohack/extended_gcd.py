def gcd(a,b):
    if a == b:
        return b
    elif b == 0:
        return a
    quotient = a //b
    reminder = a%b
    return gcd(b,reminder)

def extendedGCD(p,q):
    if p == 0:
        return q, 0 , 1
    
    gcd, x1, y1 = extendedGCD(q%p, p)

    x = y1 - (q//p) * x1
    y = x1

    return gcd, x ,y

print(extendedGCD(26513,32321))
