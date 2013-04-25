import re

def checkio(line):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    line = re.sub(' +', ' ', line)
    #replace this for solution
    return line
