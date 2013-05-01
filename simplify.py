import re
import pdb
data = "x+(x+1)*(2*x+5)*(2*x+3)-(2*x-3)*x*2-x*x+(2*x+3)*2-x+x*x*x*x-21"


def getcoef(string):
    findd = re.compile('[\+-]?[\d]*')
    degree = string.count('x')
    b = findd.search(string).group()
    if (b == '' or b == '+') :
        coef = 1
    elif b == '-':
        coef = -1
    else:
        coef = int(b)
    return degree, coef

def polycoef(data):
    term = re.compile('[\+-]?[0-9\*x]+')
    mm = term.findall(data)
    if mm == []:
        return [0]
    c = [getcoef(one) for one in mm]
    ans = [0]*(max(c)[0]+1)
    ans[c[0][0]] = c[0][1]
    for one in c[1:]:
        ans[one[0]] += one[1]
    return ans



def combine(coef1, coef2):
    l1, l2 = len(coef1), len(coef2)
    if l1 < l2:
        for i in range(l1):
            coef2[i] += coef1[i]
        return coef2
    else:
        for i in range(l2):
            coef1[i] += coef2[i]
        return coef1
        
def coef2string(coef):
    l = len(coef)
    ans = ''
    for degree in range(l - 1, 0, -1):
        term = 'x' + '*x'*(degree - 1)
        tmpcoef = coef[degree]
        if tmpcoef == 0:
            continue
        elif tmpcoef == 1:
            ans = ans + term + '+'
        elif tmpcoef == -1:
            ans = ans[:(len(ans)-1)] + '-'+term + '+'
        elif tmpcoef < 0:
            ans = ans[:(len(ans)-1)] + str(tmpcoef) + '*' + term + '+'
        else:
            ans = ans + str(tmpcoef) + '*' + term + '+'
    if coef[0] == 0:
        ans = ans[:(len(ans)-1)]
    elif coef[0] < 0:
        ans = ans[:(len(ans)-1)] + str(coef[0])
    else:
        ans = ans + str(coef[0])
    return ans

def checkio(data):
    if data[len(data) - 1] == ')':
        data = data + '+0'
    p = re.compile('[\+-]?[x\d\*]*?\(.*?\)[x\d\*]*?(?=[\+-])')
    m = p.split(data)
    l = p.findall(data)

    tmpdata = ''.join(m)
    coefall = polycoef(tmpdata)
    paren = re.compile('(?<=\().*?(?=\))')

    for a  in l:
        bb = paren.findall(a)
        notparen = re.compile('\(.*\)')
        c =  notparen.split(a)
        f = re.compile('\d+')
        degree = 0
        if c[0] == '':
            coef = 1
        else:
            if c[0][0] == '-':
                coef = -1
            else :
                coef = 1
        for one in c:
            for digit in f.findall(one):
                if not digit  == []:
                    coef *= int(digit)
            degree += one.count('x')
        ans = [0]*(degree + 1)
        ans[degree] = coef
        coef = ans
        for one in bb:
            tmp =  polycoef(one)
            tmp3 = [0]*(len(coef) + len(tmp) - 1)
            for i in range(len(tmp)):
                k = len(tmp) - 1 - i
                tmp2 = [j*tmp[k] for j in coef]
                tmp2 = [0]*k + tmp2
                for j in range(len(tmp2)):
                    tmp3[j] += tmp2[j]
            coef = tmp3
        coefall =  combine(coefall, coef)

    ans = coef2string(coefall)
    return ans

# print checkio(data)
data = "x*x*x*x*x+10-2"
print checkio(data)

