from numpy import infty, sqrt
def ClosestPair(points:list):
    n = len(points)
    closest = infty
    for i in range(n-1):
        for j in range(i+1, n):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][0]
            distance = sqrt((y2 - y1)**2 + (x2 - x1)**2)
            if distance < closest:
                I = i
                J = j
                closest = distance
    
    return closest, I, J

pts = [(0,1), (-1,1), (5, 9), (2, 0), (1, 0)]

print(ClosestPair(pts))

