def score(x, y):
    distance = x*x + y*y
    if distance > 100: return 0
    if distance > 25: return 1
    if distance > 1: return 5
    return 10
