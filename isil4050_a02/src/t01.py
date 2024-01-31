"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-09-24"
-------------------------------------------------------
"""
from Food_utilities import by_origin
from Food_utilities import read_foods
f = open('foods.txt','r')
foods = read_foods(f)
origin = 1
v = by_origin(foods, origin)
for i in v:
    print(i)