# 5. You are going to tile a room whose dimensions are length by width feet. There are twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need?
# You can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips, breakage, and mess-ups.
#  How many total boxes will you buy?

import math
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
area = length * width
tiles_needed = area * 1.10
boxes_needed = math.ceil(tiles_needed / 12)

print(f"Room area: {area:.2f} sq ft")
print(f"Tiles needed (+ 10%): {tiles_needed:.0f} tiles")
print(f"Boxes to buy:   {boxes_needed} boxes")