def leap_year(a: int) -> int:
    """
Determine if a year is a leap year or not

Args:
    a = specific year

Return:
    If leap year: a is a leap year
    else: a is not a leap year

"""
    if (a % 4) == 0:
        return f'{a} is a leap year'
    if (a % 100) == 0 and (a % 400) != 0:
        return f'{a} is a leap year'
    else:
        return f'{a} is not a leap year'
    

user_int = int(input("Enter year: "))

x = leap_year(user_int)

print(x)