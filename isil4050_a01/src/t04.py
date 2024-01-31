"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-09-18"
-------------------------------------------------------
"""
# Imports
from functions import median_scores

fv = open('numbers.txt','r')
median = median_scores(fv)
print(median)