import math

def jarak(x1, x2, y1, y2):
    d = math.sqrt(pow(x1 - x2, 2) + pow(y2 - y1, 2))
    return d
print(jarak(0, 0, 0, 5))