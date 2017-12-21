x1 = float(input('x1='))
x2 = float(input('x2='))
y1 = float(input('y1='))
y2 = float(input('y2='))


def distance(x1, y1, x2, y2):
    answer = ((x2 - x1)**2 + (y2-y1)**2)**0.5
    return answer
print(distance(x1, y1, x2, y2))