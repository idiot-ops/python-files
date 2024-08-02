def total(number1, number2):
    return number1 + number2

def main_function():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    sol = total(first_number, second_number)
    print("The total is:", sol)

def sphere_volume(radius):
    return (4/3) * 3.14 * radius**3

def sphere_volume_calculation():
    large_radius = int(input("Enter the large radius: "))
    small_radius = int(input("Enter the small radius: "))
    volume_large = sphere_volume(large_radius)
    volume_small = sphere_volume(small_radius)
    print("The volume of the sphere with the large radius is:", volume_large)
    print("The volume of the sphere with the small radius is:", volume_small)

# Run the main functions
main_function()
sphere_volume_calculation()
