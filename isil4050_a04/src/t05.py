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
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
key = 2

target1, target2 = source.split_key(key)
for i in target1:
    print(i)
for i in target2:
    print(i)