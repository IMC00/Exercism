def is_triangle(a, b, c):
    return a + b >= c and b + c >= a and c + a >= b

def equilateral(sides):
    if any(side <= 0 for side in sides):
        return False

    unique_sides = len(set(sides))
    return unique_sides == 1 and is_triangle(sides[0], sides[1], sides[2])


def isosceles(sides):
    if any(side <= 0 for side in sides):
        return False
    return len(set(sides)) <= 2 and is_triangle(sides[0], sides[1], sides[2])


def scalene(sides):
    if any(side <= 0 for side in sides):
        return False
    return len(set(sides)) == 3 and is_triangle(sides[0], sides[1], sides[2])
