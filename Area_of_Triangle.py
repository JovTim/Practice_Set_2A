def area_of_triangle(a: int, b: int, c: int) -> int:
    """
Calculate the Area of Triangle a, b, c using Heron's Formula

Args:
    a = side of triangle
    b = side of triangle
    c = side of triangle

Return:
    Area of Triangle

"""
    return (a + b + c)/ 2
    

user_a = int(input("Enter Number(a): "))
user_b = int(input("Enter Number(b): "))
user_c = int(input("Enter Number(c): "))


x = area_of_triangle(user_a, user_b, user_c)
print(f'The Area of Triangle: {x}')