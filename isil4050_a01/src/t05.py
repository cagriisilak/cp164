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
from functions import matrix_stats

a = [[1,2,3],[3,4,5]]
small, large, total, average = matrix_stats(a)
print('Small: ',small)
print('Large: ',large)
print('Total: ',total)
print('Average: ',average)
