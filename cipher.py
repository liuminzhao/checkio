#Your code here
#You can import some modules or create additional functions

import re
def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    
    grille, template = data
    coor = []
    string = ''
    p = re.compile('X')
    for i in range(4):
        a  = grille[i]
        m = p.finditer(a)
        for one in m:
            coor.append((i, one.start()))
            string += template[i][one.start()]
    
    for j in range(3):
        for i in range(4):
            one = coor[i]
            coor[i] = (one[1], 3 - one[0])
        coor = sorted(coor)
        for one in coor:
            string += template[one[0]][one[1]]
 
    #replace this for solution
    return string

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([['X...',
                     '..X.',
                     'X..X',
                     '....'],
                    ['itdf',
                     'gdce',
                     'aton',
                     'qrdi']]) == 'icantforgetiddqd', 'First example'

    assert checkio([['....',
                     'X..X',
                     '.X..',
                     '...X'],
                    ['xhwc',
                     'rsqx',
                     'xqzz',
                     'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'
