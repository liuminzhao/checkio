import math
def checkio(data):
    balance, withdrawal = data
    for one in withdrawal:
        if one > balance or one%5 or one < 0:
            continue
        else:
            charge = one + 0.5 + one*0.01
            if charge > balance :
                continue
            else:
                balance -= charge
                balance = int(balance)
    return balance
