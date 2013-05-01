data = [1,2,3]
## data = [1,[2,2,2],4]
## data = [[[2]],[4,[5,6,[6],6,6,6],7]]
ans = []
def allinrow(data):
    for one in data:
        if not isinstance(one, list):
            ans.append(one)
        else:
            ans.append(allinrow(one))


allinrow(data)
ans = [one for one in ans if not one == None]
print ans
