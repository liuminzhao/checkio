def area2(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax)*(cy - ay) - (cx - ax)*(by - ay)

data = [[0,0], [0,2], [5,1], [3,1]]
a = data[0]
b = data[1]
c = data[2]
d = data[3]

if area2(c, d, a)== 0 and area2(c, d, b) ==0:
    if b[0] <= d[0] <= c[0]:
        return True
    else:
        return False

if area2(c, d, a)*area2(c, d, b) <=0:
    if area2(a, b, c)*area2(a, b, d) <= 0:
        print True
    else: 
        if abs(area2(a, b, c)) > abs(area2(a, b, d)):
            print True
