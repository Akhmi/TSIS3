import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# Example usage:
radius = 5
volume = sphere_volume(radius)
print(f"The volume of a sphere with radius {radius} units is {volume} cubic units.")
#The volume of a sphere with radius 5 units is 523.5987755982989 cubic units.