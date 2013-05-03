__author__ = 'liuminzhao'

def checkio(data):
    input, output, newinput = data

    inputnum = []
    outputnum = []

    for one in input:
        if one == ' ':
            inputnum.append(0)
        else:
            inputnum.append(ord(one)-96)

    for one in output:
        if one == ' ':
            outputnum.append(0)
        else:
            outputnum.append(ord(one)-96)


    diffnum = [(j - i)%27 for (i, j) in zip(inputnum, outputnum)]

    k = 1
    flag = 0
    for k in range(1, len(inputnum)/2):
        if diffnum[0:k] == diffnum[k:(2*k)] and diffnum[(k):(2*k)] == diffnum[(2*k):(3*k)]:
            flag = 1
            break
    secret = diffnum[0:k]
    if not flag:
        for k in range(1, len(inputnum)/2):
            if diffnum[0:k]== diffnum[::-1][0:k][::-1]:
                flag = 1
                secret = diffnum[0:(len(diffnum) - k)]
                k = len(diffnum) - k
                break
        if not flag:
            k = len(diffnum)
            secret = diffnum

    newinputnum = []
    i = 0

    for one in newinput:
        if one == ' ':
            newinputnum.append((0 + secret[i%k])%27)
        else:
            newinputnum.append((ord(one)-96 + secret[i%k])%27)
        i += 1

    newoutput = ''
    for one in newinputnum:
        if one == 0:
            newoutput += ' '
        else:
            newoutput += chr(one + 96)

    return newoutput

print checkio(
        [
            'vjwclkjfijm',
            'keyofsecret',
            'lpcmuyxhuwyd'
        ])