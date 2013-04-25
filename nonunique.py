def checkio(data):
    uniquelist = [one for one in data if data.count(one) == 1]
    for one in uniquelist:
        data.remove(one)
    return data
