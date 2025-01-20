# Task 4: Given the legs of a right triangle. Find its hypotenuse and area.

a = 3  # leg a
b = 4  # leg b

c = ((a ** 2 + b ** 2) ** 0.5)  # formula for calculating hypotenuse
area = a * b / 2

print("Hypotenuse is", c, "\n"
      "Area is", area
      )
