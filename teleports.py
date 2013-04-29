## teleports_string = "12,23,34,45,56,67,78,81"
## teleports_string = "12,23,34,45,56,67,78,81,17,28,33,44"
##teleports_string = "12,28,87,71,13,14,34,35,45,46,63,65"
def checkio(data):
    # The idea is to delete unused bridges and 
    # turn problem into Eulerian Path problem.
    # Since vertex 1 is both the start and end point, 
    # every vertex mush have even degrees. So for vertex
    # with odd degrees, if one pair of them are connected, 
    # delete the bridge between them and make them as vertex
    # with even degrees. Do this until number of vertex 
    # with odd degrees is zero. 
    # If none of vertex with odd degrees connects, try to find
    # the middle vertex connecting them with degrees larger 
    # or equal to four. If we find one or two middle vertex, 
    # delete the bridges between odd-degree vertex and middle
    # vertex, thus making them as even-degree vertex.
    
    # After deleting unused bridges and making all vertex with
    # even degrees, we apply the eular path algorithm to find
    # the loop.

    # transfer bridge into matrix (road)
    road = [[0 for i in range(8) ] for j in range(8)]
    a = data.split(',')
    for one in a:
        x, y = int(one[0]), int(one[1])
        road[x - 1][y - 1] = 1
        road[y - 1][x - 1] = 1

    # stack, circuit, location for euler path problem
    # location is the current location
    stack = []
    circuit = []
    location = 0

    # odd are the vertex with odd degrees
    # p is the number of those vertex
    odd = [one for one in range(8) if sum(road[one])%2]
    p = len(odd)

    while not p == 0:
        flag = 0
        # If any of the odd-degree vertex connects, delete 
        # the bridge between them
        for i in range(p):
            for j in range(i+1, p):
                if road[odd[i]][odd[j]] == 1:
                    road[odd[i]][odd[j]] = 0
                    road[odd[j]][odd[i]] = 0
                    odd = [one for one in range(8) if sum(road[one])%2]
                    p = len(odd)
                    flag = 1
                if flag:
                    break

        # If none of the odd-degree vertex connects, 
        # find the middle vertex, and delete the whole bridge
        if not flag:
            mid0 = [one for one in range(8) if road[odd[0]][one] == 1 and sum(road[one]) >= 4]
            mid1 = [one for one in range(8) if road[odd[1]][one] == 1 and sum(road[one]) >= 4]
            for i in mid0:
                for j in mid1:
                    if i == j:
                        road[i][odd[0]] = 0
                        road[i][odd[1]] = 0
                        road[odd[0]][i] = 0
                        road[odd[1]][i] = 0
                        flag = 1
                    elif road[i][j] == 1:
                        road[i][odd[0]] = 0
                        road[j][odd[1]] = 0
                        road[odd[0]][i] = 0
                        road[odd[1]][j] = 0
                        road[i][j] = 0
                        road[j][i] = 0
                        flag = 1
                    odd = [one for one in range(8) if sum(road[one])%2]
                    p = len(odd)
                    if flag:
                        break

    # Apply Euler path algorithm 
    while 1:
        if road[location].count(1) == 0:
            circuit.append(location + 1)
            location = stack.pop()
        else:
            stack.append(location)
            nextpoint = road[location].index(1)
            road[location][nextpoint] = 0
            road[nextpoint][location] = 0
            location = nextpoint
        if road[location].count(1) == 0 and stack == []:
            break

    return ''.join([str(one) for one in  circuit]) + '1'

print checkio("12,23,34,45,56,67,78,81") 
print checkio("12,28,87,71,13,14,34,35,45,46,63,65") 
print checkio("12,28,87,71,13,14,34,35,45,46,63") 
print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") 
print checkio("12,15,16,23,24,28,83,85,86,71,74") 
print checkio("13,14,23,25,34,35,47,56,58,76,68") 
