import math

print(
"""==================
Area Calculator 
==================\n""")

print(
"""Choose a shape to calculate the area:

1) Triangle
2) Rectangle   
3) Square
4) Circle
5) Quit\n""")

options = int(input("Your choice: "))

if options == 1: # Triangle
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (height * base) / 2
    print(f"The area is {area}")
elif options == 2: # Rectangle
    length = float(input("Length: ")) # Length 
    width = float(input("Width: ")) # Width 
    area = length * width
    print(f"The area is {area}")
elif options == 3: # Square
    side = float(input("Side: "))
    area = side ** 2
    print(f"The area is {area}")
elif options == 4: # Circle
    radius = float(input("Radius: "))
    area = math.pi * radius ** 2
    print(f"The area is {area}")
elif options == 5: # Quit
    print("Exiting the calculator. Goodbye!")
else:
    print("Invalid option. Please choose a valid shape.")
