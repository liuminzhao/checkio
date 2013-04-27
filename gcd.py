# from fractions import gcd
# gcd(data[0], data[1])
def checkio(data):
    n1, n2 = data
    p = min(n1, n2)
    while n1%p or n2%p:
        p -= 1
    return p

print checkio((12, 8))
print checkio((14, 21))
print checkio((13, 11))
