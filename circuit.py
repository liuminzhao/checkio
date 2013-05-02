def checkio(data):

    def coor(n):
        k = 1
        if n == 1:
            return (0, 0)
        while not (2*k-1)**2 < n <= (2*k+1)**2:
            k += 1
        edge = 2*k
        remind = ((2*k+1)**2 - n)%edge
        div = ((2*k+1)**2 - n)/edge
        ans = (0, 0)
        if div == 0:
            ans = (-k, k - remind)
        elif div == 1:
            ans = (-k + remind, -k)
        elif div == 2:
            ans = (k, -k + remind)
        else:
            ans = (k - remind, k)
        return ans

    x = coor(data[0])
    y = coor(data[1])
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

print checkio([1, 9])