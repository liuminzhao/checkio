import itertools

def checkio(data):
    n = len(data)
    total = sum(data)
    if n == 1:
        return data[0]
    mindiff = 100
    for i in range(1, n/2 + 1):
        a = itertools.combinations(data, i)
        for one in a:
            diff = abs(2*sum(one) - total) 
            if diff < mindiff:
                mindiff = diff
    return mindiff


