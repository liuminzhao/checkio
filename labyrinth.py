#Your code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    x, y = 1, 1
    last = 'S'
    string = ''
    while not ( x == 10 and y == 10) :
        if last == 'S':
            if data[x][y - 1] == 0:
                string += 'W'
                last = 'W'
                y -= 1
            else:
                if data[x+1][y] == 0 :
                    string += 'S'
                    x += 1
                    last = 'S'
                else:
                    if data[x][y+1] == 0:
                        string += 'E'
                        last = 'E'
                        y += 1
                    else:
                        string += 'N'
                        last = 'N'
                        x -= 1
        if last == 'W':
            if data[x-1][y] == 0:
                string += 'N'
                last = 'N'
                x -= 1
            else:
                if data[x][y-1] == 0 :
                    string += 'W'
                    y -= 1
                    last = 'W'
                else:
                    if data[x+1][y] == 0:
                        string += 'S'
                        last = 'S'
                        x += 1
                    else:
                        string += 'E'
                        last = 'E'
                        y += 1
        if last == 'N':
            if data[x][y+1] == 0:
                string += 'E'
                last = 'E'
                y += 1
            else:
                if data[x-1][y] == 0 :
                    string += 'N'
                    x -= 1
                    last = 'N'
                else:
                    if data[x][y-1] == 0:
                        string += 'W'
                        last = 'W'
                        y -= 1
                    else:
                        string += 'S'
                        last = 'S'
                        x += 1
        if last == 'E':
            if data[x+1][y] == 0:
                string += 'S'
                last = 'S'
                x += 1
            else:
                if data[x][y+1] == 0 :
                    string += 'E'
                    y += 1
                    last = 'E'
                else:
                    if data[x-1][y] == 0:
                        string += 'N'
                        last = 'N'
                        x -= 1
                    else:
                        string += 'W'
                        last = 'W'
                        y -= 1


    #replace this for solution
    #This is just example for first maze
    return string

#Some hints
#Look to graph search algorithms
#Don't confuse these with tree search algorithms


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    #be carefull with infinity loop
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]))
