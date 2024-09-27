def gcd(a,b):
    if a == b:
        return b
    elif b == 0:
        return a
    quotient = a //b
    reminder = a%b
    return gcd(b,reminder)

print(gcd(66528,52920))
