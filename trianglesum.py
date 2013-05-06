# data = [[0 for i in range(15)] for j in range(15)]

def checkio(dat):
    l = len(dat)
    total = 0
    for i in range(2):
        dat[1][i] +=  dat[0][0]

    for i in range(2, l):
        dat[i][0] += dat[i-1][0]
        dat[i][i] += dat[i-1][i-1]
        for j in range(1, i):
            dat[i][j] += max(dat[i-1][j-1], dat[i-1][j])
    return max(dat[l-1])
