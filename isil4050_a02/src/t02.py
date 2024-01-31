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
from Food_utilities import average_calories
from Food_utilities import read_foods
f = open('foods.txt','r')
foods = read_foods(f)
avg = average_calories(foods)
print(avg)