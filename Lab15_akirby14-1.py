'''
Name: Area of a Triangle
Author: Adryiana Kirby
Purpose: Creates an image of the area of a triangle
Date: 11/22/26
'''

import matplotlib.pyplot as plt
import math

base = 10
height = 10

area = (1 / 2) * base * height

hypotenuse = math.sqrt((base / 2) ** 2 + height ** 2)

x_values = [0, base, base / 2, 0]
y_values = [0, 0, height, 0]

plt.plot(x_values, y_values, color="purple", linewidth=2)

plt.title("Area of a Triangle")
plt.xlabel("Base Length")
plt.ylabel("Height")

plt.grid(True)

plt.text(base / 2, height / 2, f"Area = {area}", ha="center")

plt.xlim(-2, base + 2)
plt.ylim(-2, height + 2)

plt.savefig("triangle_area.png")

plt.show()