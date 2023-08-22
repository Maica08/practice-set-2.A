"""
This program contains a function that calculates
the area of a triangle using Heron's formula
"""

def area_triangle_Heron(side1: float, side2: float, side3: float) -> float:
    """
    Calculate area of a triangle with its three sides

    Args:
        side1 - refers to the first side of triangle
        side2 - refers to the second side of the triangle
        side3 - refers to the third side of the triangle
    
    Return:
        Calculated area of the triangle
    """
    s = sum([side1, side2, side3]) / 2 # s is half of the parameter of the triangle

    area = (s*(s-side1)*(s-side2)*(s-side3)) ** (1/2) # performing heron's formula

    return area


def main():
    side1 = float(input("Enter the measurement of the first side: "))
    side2 = float(input("Enter the measurement of the second side: "))
    side3 = float(input("Enter the measurement of the third side: "))

    area_triangle = area_triangle_Heron(side1, side2, side3)
    print(f"The area of the triangle is {round(area_triangle, 4)} units squared.")

if __name__ == "__main__":
    main()

