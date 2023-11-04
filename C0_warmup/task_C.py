import math

x_1, y_1, x_2, y_2 = map(int, input().split())


def angle_between_points(x1, y1, x2, y2):
    alpha_rad = math.atan2(y1, x1) - math.atan2(y2, x2)
    return alpha_rad

def short_long_radius(x1, y1, x2, y2):
    r1 = math.sqrt(x1*x1 + y1*y1)
    r2 = math.sqrt(x2*x2 + y2*y2)
    if r1 < r2:
        return r1, r2
    else:
        return r2, r1

def arc_length(angle_between, radius):
    L = radius * math.fabs(angle_between)
    return L

def path_by_radius(radius1, radius2):
    return radius1+radius2

def path_by_arc(angle_between, radius_short, radius_long):
    L = arc_length(angle_between, radius_short)
    return L + radius_long - radius_short

def find_shortest_path(x1, y1, x2, y2):
    angle_rad = angle_between_points(x1, y1, x2, y2)
    short_r, long_r = short_long_radius(x1, y1, x2, y2)
    way_r = path_by_radius(short_r, long_r)
    way_a = path_by_arc(angle_rad, short_r, long_r)
    if way_a < way_r:
        print(way_a)
    else:
        print(way_r)

find_shortest_path(x_1, y_1, x_2, y_2)