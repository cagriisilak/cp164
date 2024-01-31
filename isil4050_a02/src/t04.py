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
from Food_utilities import food_table
from Food_utilities import read_foods
f = open('foods.txt','r')
foods = read_foods(f)
food_table(foods)