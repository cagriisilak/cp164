"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-09"
-------------------------------------------------------
"""
from Queue_array import Queue

source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)

target1, target2 = source.split_alt()
for i in target1:
    print(i)
for i in target2:
    print(i)