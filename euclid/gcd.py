
def gcd(m, n):
    a = m
    b = n
    while b != 0:
        a, b = b, a % b
    return a
    
