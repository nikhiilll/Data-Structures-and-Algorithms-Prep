from operator import itemgetter

def minTimeToVisitAllPoints(points):

    time = 0

    for i in range(len(points) - 1):

        x1, y1 = itemgetter(0, 1)(points[i])
        x2, y2 = itemgetter(0, 1)(points[i + 1])
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        if x_diff <= y_diff:
            time += y_diff
        else:
            time += x_diff
    
    return time

points = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))

