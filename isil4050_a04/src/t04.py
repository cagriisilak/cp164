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
from Queue_circular import Queue
from functions import pq_split_key

source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
key = 2

target1, target2 = pq_split_key(source, key)
for i in target1:
    print(i)
for i in target2:
    print(i)