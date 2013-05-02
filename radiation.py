__author__ = 'liuminzhao'

data = [
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]
]

def checkio(data):
    m = len(data)
    n = len(data[0])

    node = [(x, y) for x in range(m) for y in range(n) ]

    totalmarked = []
    maxlen = 0
    maxvalue = 0

    def adjacent(t):
        x, y = t
        return [(max(x-1, 0), y), (min(x+1, m-1), y), (x, max(0, y-1)), (x, min(n-1, y+1))]

    for onenode in node:
        if not onenode in totalmarked:
            queue = [onenode]
            marked = [onenode]
            value = data[marked[0][0]][marked[0][1]]

            while not queue == []:
                t = queue.pop(0)
                for neighbour in adjacent(t):
                    if not neighbour in marked and data[neighbour[0]][neighbour[1]] == value:
                        marked.append(neighbour)
                        queue.append(neighbour)

            if  len(marked) > maxlen:
                maxlen = len(marked)
                maxvalue = value
            for one in marked:
                totalmarked.append(one)

    return [maxlen, maxvalue]

print checkio(data)