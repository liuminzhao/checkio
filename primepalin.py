import math

def ispalin(n):
    string = str(n)
    if string == string[::-1]:
        return True
    else:
        return False

def isprime(x):
    return not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]

def checkio(data):
    while not (isprime(data) and ispalin(data)) : 
        data += 1
    return data

print checkio(31)
print checkio(130)
print checkio(131)
