#Your code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
    print data
    if data[0] >= data[2]:
        return(data[0])
    elif data[0] + data[1] >= data[2]:
        return(data[2])
    elif data[0] > data[2] - data[3]:
        return(data[0])
    else:
        return(checkio([data[0] + data[1], data[1], data[2]-data[3], data[3]]))

    #replace this for solution
    return 0

#Some hints
#Be careful with endless loop


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"
