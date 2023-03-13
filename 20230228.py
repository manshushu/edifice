r = float(input("Radius:"))

s= 3.14 * r ** 2

if r>=0:
    print(s)

else:
    print("Radius muat greater than...")

def print_list(lst):
    for element in lst:
        print(element)

my_list = [1, 2, 3, 4, 5]
print_list(my_list)
