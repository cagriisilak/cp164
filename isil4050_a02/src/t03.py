"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
from Food_utilities import calories_by_origin
from Food_utilities import read_foods
f = open('foods.txt','r')
foods = read_foods(f)
origin = 3
a = calories_by_origin(foods, origin)
print(a)