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
from Food_utilities import food_search
from Food_utilities import read_foods
f = open('foods.txt','r')
foods = read_foods(f)
origin = 1
max_cals = 200
is_veg = False
results = food_search(foods, origin, max_cals, is_veg)
for i in results:
    print(i)