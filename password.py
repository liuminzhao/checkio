def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    if len(data) < 10 :
        return False
    else:
        digit = [one.isdigit() for one in data]
        if not any(digit):
            return False
        else:
            lower = [one.islower() for one in data]
            if not any(lower):
                return False
            else:
                upper = [one.isupper() for one in data]
                if not any(upper):
                    return False
                    
    #replace this for solution
    return True 
