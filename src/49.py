import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def perimeter_of_circle(radius):
    return 2 * math.pi * radius

def volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def calculate_angle_between_points(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    if x1 > x2:
        return int(angle + 360)
    else:
        return int(angle)

def main():
    # Example usage
    radius = 5
    print("Area of circle:", area_of_circle(radius))
    print("Perimeter of circle:", perimeter_of_circle(radius))
    print("Volume of cylinder:", volume_of_cylinder(3, 4))

if __name__ == "__main__":
    main()
