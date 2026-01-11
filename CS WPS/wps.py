def fastGCD(x, y):
    big = max(x,y)
    small = min(x,y)
    rem = big % small

    while (rem != 0):
        big = small
        small = rem
        rem = big % small
        
    return small

def threeGCD(x, y, z):
    gcd = fastGCD(x, fastGCD(y, z))

    return gcd
