def convexHull(points):
    n = len(points)
    hull = set()
    for i in range(n):
        for j in range(i, n):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][0]
            a = x1 - y2
            b = x2 - x1
            c = x1*y2 - x2*y1
            for k in range(n - 1):
                if (k != i and k != j):
                    print('falta terminar')