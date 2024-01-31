"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-02"
-------------------------------------------------------
"""
from Stack_array import Stack
source = Stack()
source.push(1)
source.push(3)
source.push(5)
source.push(7)

for i in source:
    print(i)

source.reverse()

for i in source:
    print(i)