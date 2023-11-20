import math

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is {:.2f}".format(area))

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print("The area of the circle is {:.2f}".format(area))

def main():
    shape_type = input("Enter the shape type: ")
    get_area(shape_type)

if __name__ == "__main__":
    main()
