# function to find the area of a triangle using Heron's formula
def heron_formula(a, b, c):
    # calculate the semiperimeter of the triangle
    s = (a + b + c) / 2

    # calculate the area of the triangle using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # return the calculated area
    return area


# sample side lengths of a triangle

a = 4
b = 5
c = 6
list1 = [a, b, c]
# print the area of the triangle
print("Area of the triangle is:", heron_formula(list1[0], list1[1], list1[2]))
